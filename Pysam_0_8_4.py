from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class PysamInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing PySam 0.8.4 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/pysam')
                        node.ssh.execute('pip install --target=d:\/opt/software/pysam pysam') #https://github.com/pysam-developers/pysam/archive/v0.8.4.tar.gz')
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/pysam/;touch /usr/local/Modules/applications/pysam/0.8.4')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/pysam/0.8.4')
			node.ssh.execute('echo "set root /opt/software/pysam/pysam-0.8.4" >> /usr/local/Modules/applications/pysam/0.8.4')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/pysam/0.8.4')
