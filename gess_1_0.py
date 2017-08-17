from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class GessInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing GESS 1.0 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/gess/1.0 http://compbio.uthscsa.edu/GESS_Web/files/gess.src.tar.gz')
			node.ssh.execute('cd /opt/software/gess/1.0/ && tar xzf /opt/software/gess/1.0/gess.src.tar.gz')
			node.ssh.execute('chmod +x /opt/software/gess/1.0/gess/GESS.py')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/gess/;touch /usr/local/Modules/applications/gess/1.0')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/gess/1.0')
			node.ssh.execute('echo "set root /opt/software/gess/1.0/gess" >> /usr/local/Modules/applications/gess/1.0')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/gess/1.0')
			
