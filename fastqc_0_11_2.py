from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class FastQCInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing fastqc 0.11.2 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/fastqc http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.2.zip')
			node.ssh.execute('unzip -d /opt/software/fastqc/0.11.2 /opt/software/fastqc/fastqc_v0.11.2.zip')
			node.ssh.execute('chmod 755 /opt/software/fastqc/0.11.2/FastQC/fastqc')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/fastqc/;touch /usr/local/Modules/applications/fastqc/0.11.2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/fastqc/0.11.2')
			node.ssh.execute('echo "set root /opt/software/fastqc/0.11.2/FastQC" >> /usr/local/Modules/applications/fastqc/0.11.2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/fastqc/0.11.2')