from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class QoRTsInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing QoRTs 0.3.17 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/qorts https://github.com/hartleys/QoRTs/releases/download/v0.3.17/QoRTs_0.3.17.zip')
			node.ssh.execute('cd /opt/software/qorts && unzip QoRTs_0.3.17.zip')
			node.ssh.execute('chmod +x /opt/software/qorts/QoRTs_0.3.17/QoRTs.jar')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/qorts/;touch /usr/local/Modules/applications/qorts/0.3.17')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/qorts/0.3.17')
			node.ssh.execute('echo "set root /opt/software/qorts/QoRTs_0.3.17" >> /usr/local/Modules/applications/qorts/0.3.17')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/qorts/0.3.17')
			
