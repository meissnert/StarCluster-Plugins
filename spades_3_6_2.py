from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SPAdesInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing SPAdes 3.6.2 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/spades/3.6.2')
			node.ssh.execute('wget -c -P /opt/software/spades/3.6.2 http://spades.bioinf.spbau.ru/release3.6.2/SPAdes-3.6.2-Linux.tar.gz')
			node.ssh.execute('cd /opt/software/spades/3.6.2 && tar -zxf SPAdes-3.6.2-Linux.tar.gz')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/spades/;touch /usr/local/Modules/applications/spades/3.6.2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/spades/3.6.2')
			node.ssh.execute('echo "set root /opt/software/spades/3.6.2" >> /usr/local/Modules/applications/spades/3.6.2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/spades/3.6.2')
