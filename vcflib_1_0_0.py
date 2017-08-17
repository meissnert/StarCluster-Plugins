from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class vcflibInstaller(ClusterSetup):
        def run(self, nodes, master, user, user_shell, volumes):
                for node in nodes:
                        log.info("Installing vcflib 1.0 on %s " % (node.alias))
                        node.ssh.execute('mkdir -p /opt/software/vcflib')
                        node.ssh.execute('cd /opt/software/vcflib && git clone --recursive git://github.com/ekg/vcflib.git')
                        node.ssh.execute('cd /opt/software/vcflib/vcflib/ && make')
                        node.ssh.execute('mv /opt/software/vcflib/vcflib /opt/software/vcflib/vcflib_1.0')

                        node.ssh.execute('mkdir -p /usr/local/Modules/applications/vcflib/;touch /usr/local/Modules/applications/vcflib/1.0')
                        node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/vcflib/1.0')
                        node.ssh.execute('echo "set root /opt/software/vcflib/vcflib_1.0" >> /usr/local/Modules/applications/vcflib/1.0')
                        node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/vcflib/1.0')
