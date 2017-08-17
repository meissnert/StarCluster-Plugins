from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BBMapInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing BBMap 33.73b on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/bbmap/33.73b')
			node.ssh.execute('wget -c -P /opt/software/bbmap/ http://sourceforge.net/projects/bbmap/files/BBMap_33.73b_java7.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/bbmap/BBMap_33.73b_java7.tar.gz -C /opt/software/bbmap/33.73b')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/bbmap/;touch /usr/local/Modules/applications/bbmap/33.73b')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/bbmap/33.73b')
			node.ssh.execute('echo "set root /opt/software/bbmap/33.73b/bbmap" >> /usr/local/Modules/applications/bbmap/33.73b')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/bbmap/33.73b')
