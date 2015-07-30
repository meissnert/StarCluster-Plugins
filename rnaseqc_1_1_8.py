from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class RNASeQCInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing RNA-SeQC 1.1.8 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/rnaseqc/1.1.8 http://www.broadinstitute.org/cancer/cga/tools/rnaseqc/RNA-SeQC_v1.1.8.jar')
			node.ssh.execute('chmod +x /opt/software/rnaseqc/1.1.8/RNA-SeQC_v1.1.8.jar')
			node.ssh.execute('cp /opt/software/rnaseqc/1.1.8/RNA-SeQC_v1.1.8.jar /opt/software/rnaseqc/1.1.8/RNA-SeQC.jar')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/rnaseqc/;touch /usr/local/Modules/applications/rnaseqc/1.1.8')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/rnaseqc/1.1.8')
			node.ssh.execute('echo "set root /opt/software/rnaseqc/1.1.8" >> /usr/local/Modules/applications/rnaseqc/1.1.8')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/rnaseqc/1.1.8')
			
