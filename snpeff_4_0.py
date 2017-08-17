from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SnpEffInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing SnpEff and SnpSift 4.0 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/snpeff')
			node.ssh.execute('wget -c -P /opt/software/snpeff http://sourceforge.net/projects/snpeff/files/snpEff_v4_0_core.zip')
			node.ssh.execute('unzip /opt/software/snpeff/snpEff_v4_0_core.zip -d /opt/software/snpeff/4.0')
			node.ssh.execute('chmod +x /opt/software/snpeff/4.0/snpEff/snpEff.jar')
			node.ssh.execute('chmod +x /opt/software/snpeff/4.0/snpEff/SnpSift.jar')
			
			log.info("Creating SnpEff Module")
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/snpeff/;touch /usr/local/Modules/applications/snpeff/4.0')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/snpeff/4.0')
			node.ssh.execute('echo "set root /opt/software/snpeff/4.0/snpEff" >> /usr/local/Modules/applications/snpeff/4.0')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/snpeff/4.0')
