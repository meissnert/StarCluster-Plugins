from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class MetaSVInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing MetaSV 0.3 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/metasv/0.3')
			node.ssh.execute('cd /opt/software/metasv/0.3 && git clone https://github.com/bioinform/metasv.git')
			node.ssh.execute('cd /opt/software/metasv/0.3/metasv && python setup.py install') 
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/metasv/;touch /usr/local/Modules/applications/metasv/0.3')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/metasv/0.3')
			node.ssh.execute('echo "set root /opt/software/metasv/metasv" >> /usr/local/Modules/applications/metasv/0.3')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/metasv/0.3')
