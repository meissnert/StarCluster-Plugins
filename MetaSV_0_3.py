from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class MetaSVInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing MetaSV 0.3 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/metasv')
			node.ssh.execute('pip install --target=d:\/opt/software/metasv https://github.com/bioinform/metasv/archive/0.3.tar.gz')
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/metasv/;touch /usr/local/Modules/applications/metasv/0.3')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/metasv/0.3')
			node.ssh.execute('echo "set root /opt/software/metasv/metasv-0.3" >> /usr/local/Modules/applications/metasv/0.3')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/metasv/0.3')
