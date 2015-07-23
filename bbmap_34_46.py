from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BBMapInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing BBMap 34.46 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/bbmap/34.46')
			node.ssh.execute('wget -c -P /opt/software/bbmap/ http://tcpdiag.dl.sourceforge.net/project/bbmap/BBMap_34.46.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/bbmap/BBMap_34.46.tar.gz -C /opt/software/bbmap/34.46')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/bbmap/;touch /usr/local/Modules/applications/bbmap/34.46')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/bbmap/34.46')
			node.ssh.execute('echo "set root /opt/software/bbmap/34.46/bbmap" >> /usr/local/Modules/applications/bbmap/34.46')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/bbmap/34.46')
