from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log
import re

local_pe_attrs = {
    'pe_name':            'local',
    'slots':              '999',
    'user_lists':         'NONE',
    'xuser_lists':        'NONE',
    'start_proc_args':    'NONE',
    'stop_proc_args':     'NONE',
    'allocation_rule':    '$pe_slots',
    'control_slaves':     'TRUE',
    'job_is_first_task':  'TRUE',
    'urgency_slots':      'min',
    'accounting_summary': 'TRUE',
}

global_attrs = {
    'qmaster_params':     'ENABLE_RESCHEDULE_SLAVE=1',
    'load_report_time':   '00:00:40',
    'max_unheard':        '00:02:00',
    'reschedule_unknown': '00:05:00',
}


class SGEConfig(ClusterSetup):
    """Apply additional configuration to a running SGE instance.
       This plugin is mean to run after the build-in SGE plugin of StarCluster.
    """
    
    def __init__(self):
        pass
    
    def run (self, nodes, master, user, user_shell, volumes):
        sge = SGE(master)
        if not sge.is_installed():
            log.error("SGE is not installed on this AMI, skipping...")
            return
        
        log.info("Applying additional SGE configuration...")
        sge.create_or_update_pe('local', local_pe_attrs, ['all.q'])
        sge.update_global_config(global_attrs)
        sge.cleanup()

    def on_add_node(self, node, nodes, master, user, user_shell, volumes):
        # This code configures a specific user and group id for the user that
        # you wish to run the jobs under (if it's not sgeadmin).
        # Enable and customize as needed
        #mgroup = 'mygroup'
        #myuser = 'myuser'
        #node.ssh.execute('addgroup --system --gid 1014 %s' % mygroup) 
        #node.ssh.execute('adduser --gid 1014 --uid 1014 %s --system' % myuser)
        pass


class SGE(object):
    def __init__(self, master):
        self.mssh = master.ssh
        self.cleanup_dirs = []

    def is_installed(self):        
        return self.mssh.isdir("/opt/sge6-fresh")
        
        
    def cleanup(self):
        log.debug("Need to cleanup %s", self.cleanup_dirs)
        
    def exists_pe(self, pe_name):
        """Check if parallel environment exists"""
        spl = self.mssh.execute("qconf -spl")
        return pe_name in spl

    def create_or_update_pe(self, name, attrs, queues=None):
        """Create or update parallel environment with the specified attributes.
           Any attributes of an existing PE are replaced with the provided dict.
        """
        file = self._stage_attrs(name, attrs)
        
        if self.exists_pe(name):
            mode="M"
            verb = 'Updating'
        else:
            mode="A"
            verb = 'Creating'

        log.info("%s SGE parallel environment '%s'" % (verb, name))
        self.mssh.execute("qconf -{mode}p {file}".format(mode=mode, file=file))
        
        if queues: 
            qs=','.join(queues)
            log.info("Adding parallel environment '%s' to queues '%s'", name, qs)
            self.mssh.execute('qconf -mattr queue pe_list "%s" %s' % (name, qs))
    
        
    def update_global_config(self, attrsDict):
        """Update global config with specified attributes."""
        dir=self._create_tmp_dir()
        file="{dir}/{name}".format(dir=dir, name='global')
        sed_cmd_template="s/^({key})(\s+)(.*)/\\1\\2{value}/"
        sed_cmd = ""
        for k,v in attrsDict.iteritems():
            frag = sed_cmd_template.format(key=k, value=re.escape(v))
            sed_cmd += ' -e "%s"' % frag
        
        self.mssh.execute("qconf -sconf global | sed -r %s > %s" % (sed_cmd, file))
        self.mssh.execute("qconf -Mconf %s" % file)


    def _stage_attrs(self, fileName, attrsDict):
        dir=self._create_tmp_dir()
        file="{dir}/{name}".format(dir=dir, name=fileName)
        log.debug("Checking for file %s", file)
        f = self.mssh.remote_file(file, mode="w")
        f.writelines(self._format_attrs(attrsDict))
        f.close()
        return file
        
    def _format_attrs(self, attrsDict):
        """Format dictionary of attributes into a list of lines in the sge_config format.
        """
        return ["%s\t\t\t%s\n" % (k,v) for k,v in attrsDict.iteritems()]

    def _create_tmp_dir(self):
        dir=self.mssh.execute("mktemp --tmpdir=/tmp --directory sgeconf.XXXXXXX")
        if not dir:
            raise Exception("Failed to create temp directory")
        #master.ssh.execute("ls /tmp" % dir)
        self.cleanup_dirs.append(dir)
        return dir[0]


        
