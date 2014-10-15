from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class TophatInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Tophat 2.0.12 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/tophat http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.12.Linux_x86_64.tar.gz')
			node.ssh.execute('tar xvzf /opt/software/tophat/tophat-2.0.12.Linux_x86_64.tar.gz -C /opt/software/tophat')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/tophat/;touch /usr/local/Modules/applications/tophat/2.0.12')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/tophat/2.0.12')
			node.ssh.execute('echo "set root /opt/software/tophat/tophat-2.0.12.Linux_x86_64" >> /usr/local/Modules/applications/tophat/2.0.12')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/tophat/2.0.12')