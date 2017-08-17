from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class DellyInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Delly 0.5.9 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/delly/0.5.9')
			node.ssh.execute('wget -c -P /opt/software/delly/0.5.9 https://github.com/tobiasrausch/delly/releases/download/v0.5.9/delly_v0.5.9_linux_x86_64bit')
			node.ssh.execute('chmod +x /opt/software/delly/0.5.9/delly_v0.5.9_linux_x86_64bit')
			node.ssh.execute('mv /opt/software/delly/0.5.9/delly_v0.5.9_linux_x86_64bit /opt/software/delly/0.5.9/delly')

			log.info('Creating module file ..')
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/delly/;touch /usr/local/Modules/applications/delly/0.5.9')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/delly/0.5.9')
			node.ssh.execute('echo "set root /opt/software/delly/0.5.9" >> /usr/local/Modules/applications/delly/0.5.9')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/delly/0.5.9')