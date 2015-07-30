from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SalmonInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Salmon 0.3.0 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/salmon/0.3.0/')
			node.ssh.execute('wget -c -P /opt/software/salmon/ https://github.com/kingsfordgroup/sailfish/releases/download/v0.3.0/SalmonBeta-v0.3.0_ubuntu-12.04.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/salmon/SalmonBeta-v0.3.0_ubuntu-12.04.tar.gz -C /opt/software/salmon/0.3.0/')
			node.ssh.execute('chmod +x /opt/software/salmon/0.3.0/SalmonBeta-latest_ubuntu-12.04/bin/salmon')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/salmon/;touch /usr/local/Modules/applications/salmon/0.3.0')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/salmon/0.3.0')
			node.ssh.execute('echo "set root /opt/software/salmon/0.3.0/SalmonBeta-latest_ubuntu-12.04/" >> /usr/local/Modules/applications/salmon/0.3.0')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/salmon/0.3.0')
