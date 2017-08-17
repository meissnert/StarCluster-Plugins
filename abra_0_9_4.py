from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class AbraInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing abra v0.94 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/abra/0.94')
			node.ssh.execute('wget -c -P /opt/software/abra/0.94 https://github.com/mozack/abra/releases/download/v0.94/abra-0.94-SNAPSHOT-jar-with-dependencies.jar')
			node.ssh.execute('mv /opt/software/abra/0.94/abra-0.94-SNAPSHOT-jar-with-dependencies.jar /opt/software/abra/0.94/abra.jar')
			node.ssh.execute('chmod +x /opt/software/abra/0.94/abra.jar')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/abra/;touch /usr/local/Modules/applications/abra/0.94')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/abra/0.94')
			node.ssh.execute('echo "set root /opt/software/abra/0.94" >> /usr/local/Modules/applications/abra/0.94')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/abra/0.94')
