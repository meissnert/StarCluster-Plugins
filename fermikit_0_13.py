from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class fermikitInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing fermikit 0.13 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/fermikit/0.13 https://github.com/lh3/fermikit/releases/download/v0.13/fermikit-0.13_x64-linux.tar.bz2')
			node.ssh.execute('tar xjvf /opt/software/fermikit/0.13/fermikit-0.13_x64-linux.tar.bz2 -C /opt/software/fermikit/0.13')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/fermikit/;touch /usr/local/Modules/applications/fermikit/0.13')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/fermikit/0.13')
			node.ssh.execute('echo "set root /opt/software/fermikit/0.13/fermi.kit" >> /usr/local/Modules/applications/fermikit/0.13')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/fermikit/0.13')