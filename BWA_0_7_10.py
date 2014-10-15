from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BWAInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing BWA 0.7.10 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/bwa http://sourceforge.net/projects/bio-bwa/files/bwa-0.7.10.tar.bz2')
			node.ssh.execute('tar -xvjpf /opt/software/bwa/bwa-0.7.10.tar.bz2 -C /opt/software/bwa/')
			node.ssh.execute('make -C /opt/software/bwa/bwa-0.7.10')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/bwa/;touch /usr/local/Modules/applications/bwa/0.7.10')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/bwa/0.7.10')
			node.ssh.execute('echo "set root /opt/software/bwa/bwa-0.7.10" >> /usr/local/Modules/applications/bwa/0.7.10')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/bwa/0.7.10')