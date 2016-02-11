from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class PindelInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Pindel v0.2.0 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/pindel')
			node.ssh.execute('wget -c -P /opt/software/pindel http://www.ebi.ac.uk/~kye/pindel/v_0.2.0/BWA_BAM_2_PINDEL.tar.gz')
			node.ssh.execute('cd /opt/software/pindel && tar -zxvf BWA_BAM_2_PINDEL.tar.gz')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/pindel/;touch /usr/local/Modules/applications/pindel/v0.2.0')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/pindel/v0.2.0')
			node.ssh.execute('echo "set root /opt/software/pindel/pindel-0.2.0" >> /usr/local/Modules/applications/pindel/v0.2.0')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/pindel/v0.2.0')
