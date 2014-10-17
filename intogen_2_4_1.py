from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class IntogenInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Intogen 2.4.1 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/intogen')
			node.ssh.execute('wget -c -P /opt/software/intogen/ https://bitbucket.org/intogen/mutations-analysis/get/master.tar.gz')
			node.ssh.execute('tar xzvf /opt/software/intogen/master.tar.gz -C /opt/software/intogen/')
			node.ssh.execute('apt-get -y install swig')
			node.ssh.execute('sed -i '11s|$ROOT_PATH/data|/data/database/intogen|g' /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/setup')
			node.ssh.execute('cd /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/ && ./setup')
			node.ssh.execute('rm -r /data') # this will be linkin in on_boot.py to database drive
						
			log.info("Creating Intogen Module")
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/intogen/;touch /usr/local/Modules/applications/intogen/2.4.1')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/intogen/2.4.1')
			node.ssh.execute('echo "set root /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/" >> /usr/local/Modules/applications/intogen/2.4.1')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/intogen/2.4.1')
