from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BowtieInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Bowtie 2.2.3 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/bowtie/ http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.3/bowtie2-2.2.3-linux-x86_64.zip')
			node.ssh.execute('unzip /opt/software/bowtie/bowtie2-2.2.3-linux-x86_64.zip -d /opt/software/bowtie/')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/bowtie/;touch /usr/local/Modules/applications/bowtie/2.2.3')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/bowtie/2.3.3')
			node.ssh.execute('echo "set root /opt/software/bowtie/bowtie2-2.2.3" >> /usr/local/Modules/applications/bowtie/2.2.3')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/bowtie/2.2.3')