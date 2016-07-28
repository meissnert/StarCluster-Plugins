from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class VarScanInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing VarScan 2.4.2 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/varscan/2.4.2')
			node.ssh.execute('wget -c -P /opt/software/varscan/2.4.2 https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar')
			node.ssh.execute('chmod +x /opt/software/varscan/2.4.2/VarScan.v2.4.2.jar')
			
			log.info("Creating VarScan Module")
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/varscan/;touch /usr/local/Modules/applications/varscan/2.4.2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/varscan/2.4.2')
			node.ssh.execute('echo "set root /opt/software/varscan/2.4.2" >> /usr/local/Modules/applications/varscan/2.4.2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/varscan/2.4.2')
