from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class RockSortInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing SAMtools rocksort 0.2.0-rc5 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /root/.local/easybuild/software/samtools/dnanexus-1.0')
			node.ssh.execute('git clone https://github.com/dnanexus/htslib.git')
			node.ssh.execute('git clone https://github.com/dnanexus/samtools.git')
			node.ssh.execute('mv samtools/* /root/.local/easybuild/software/samtools/dnanexus-1.0/')
			node.ssh.execute('cp /omics_pipe/dist/modulefiles/samtools_dnanexus-1.0 /root/.local/easybuild/modules/all/samtools/dnanexus-1.0')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/cufflinks/;touch /usr/local/Modules/applications/cufflinks/2.2.1')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/cufflinks/2.2.1')
			node.ssh.execute('echo "set root /opt/software/cufflinks/cufflinks-2.2.1.Linux_x86_64" >> /usr/local/Modules/applications/cufflinks/2.2.1')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/cufflinks/2.2.1')