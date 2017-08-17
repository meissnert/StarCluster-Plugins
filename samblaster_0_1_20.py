from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SamblasterInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing samblaster 0.1.20 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/samblaster')
			node.ssh.execute('wget -c -P /opt/software/samblaster https://github.com/GregoryFaust/samblaster/releases/download/v.0.1.20/samblaster-v.0.1.20.tar.gz')
			node.ssh.execute('tar xvzf /opt/software/samblaster/samblaster-v.0.1.20.tar.gz -C /opt/software/samblaster')
			node.ssh.execute('make -C /opt/software/samblaster/samblaster-v.0.1.20')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/samblaster/;touch /usr/local/Modules/applications/samblaster/0.1.20')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/samblaster/0.1.20')
			node.ssh.execute('echo "set root /opt/software/samblaster/samblaster-v.0.1.20" >> /usr/local/Modules/applications/samblaster/0.1.20')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/samblaster/0.1.20')
