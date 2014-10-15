from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SRAInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing SRKA Toolkit 2.3.5-2 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/sra-toolkit https://github.com/ncbi/sratoolkit/archive/v2.3.5-2.tar.gz')
			node.ssh.execute('tar xvzf /opt/software/sra-toolkit/v2.3.5-2.tar.gz -C /opt/software/sra-toolkit')
			node.ssh.execute('make -C /opt/software/sra-toolkit/sratoolkit-2.3.5-2')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/sra-toolkit/;touch /usr/local/Modules/applications/sra-toolkit/2.3.5-2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/sra-toolkit/2.3.5-2')
			node.ssh.execute('echo "set root /opt/software/sra-toolkit/sratoolkit-2.3.5-2" >> /usr/local/Modules/applications/sra-toolkit/2.3.5-2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/tools" >> /usr/local/Modules/applications/sra-toolkit/2.3.5-2')