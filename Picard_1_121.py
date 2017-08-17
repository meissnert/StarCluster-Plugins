from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class PicardInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Picard tools 1.121 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/picard https://github.com/broadinstitute/picard/releases/download/1.121/picard-tools-1.121.zip')
			node.ssh.execute('unzip -d /opt/software/picard /opt/software/picard/picard-tools-1.121.zip')
			node.ssh.execute('find /opt/software/picard/picard-tools-1.121/*.jar -exec chmod 755 {} +')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/picard/;touch /usr/local/Modules/applications/picard/1.121')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/picard/1.121')
			node.ssh.execute('echo "set root /opt/software/picard/picard-tools-1.121" >> /usr/local/Modules/applications/picard/1.121')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/picard/1.121')