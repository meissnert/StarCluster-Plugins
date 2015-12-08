from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class PindelInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Pindel v0.2.5b6 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/pindel')
			node.ssh.execute('wget -c -P /opt/software/pindel https://github.com/genome/pindel/archive/v0.2.5b6.zip')
			node.ssh.execute('cd /opt/software/pindel && unzip v0.2.5b6.zip')
			node.ssh.execute('cd /opt/software/pindel/pindel-0.2.5b6 and ./INSTALL /opt/software/samtools/samtools-1.2/htslib-1.2.1/')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/pindel/;touch /usr/local/Modules/applications/pindel/v0.2.5b6')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/pindel/v0.2.5b6')
			node.ssh.execute('echo "set root /opt/software/pindel/pindel-0.2.5b6" >> /usr/local/Modules/applications/pindel/v0.2.5b6')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/pindel/v0.2.5b6')
