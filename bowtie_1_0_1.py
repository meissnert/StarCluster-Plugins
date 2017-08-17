from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BowtieInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Bowtie 1.0.1 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/bowtie http://sourceforge.net/projects/bowtie-bio/files/bowtie/1.0.1/bowtie-1.0.1-linux-x86_64.zip')
			node.ssh.execute('unzip /opt/software/bowtie/bowtie-1.0.1-linux-x86_64.zip -d /opt/software/bowtie')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/bowtie/;touch /usr/local/Modules/applications/bowtie/1.0.1')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/bowtie/1.0.1')
			node.ssh.execute('echo "set root /opt/software/bowtie/bowtie-1.0.1" >> /usr/local/Modules/applications/bowtie/1.0.1')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/bowtie/1.0.1')