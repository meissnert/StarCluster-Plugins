from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SamtoolsInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Samtools 1.1 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/samtools')
			node.ssh.execute('wget -c -P /opt/software/samtools http://sourceforge.net/projects/samtools/files/samtools/1.1/samtools-1.1.tar.bz2')
			node.ssh.execute('tar -xvjpf /opt/software/samtools/samtools-1.1.tar.bz2 -C /opt/software/samtools/')
			node.ssh.execute('make -C /opt/software/samtools/samtools-1.1')
			node.ssh.execute('find /opt/software/samtools/samtools-1.1 -type d -exec chmod 755 {} +')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/samtools/;touch /usr/local/Modules/applications/samtools/1.1')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/samtools/1.1')
			node.ssh.execute('echo "set root /opt/software/samtools/samtools-1.1" >> /usr/local/Modules/applications/samtools/1.1')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/samtools/1.1')