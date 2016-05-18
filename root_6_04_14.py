from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class RootInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Root 6.04/14 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/root')
			node.ssh.execute('wget -c -P /opt/software/root https://root.cern.ch/download/root_v6.04.14.source.tar.gz')
			node.ssh.execute('tar -xf /opt/software/root/root_v6.04.14.source.tar.gz -C /opt/software/root/')
			node.ssh.execute('cd /opt/software/root/root-6.04.14 && ./configure')
			node.ssh.execute('cd /opt/software/root/root-6.04.14 && make')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/root/;touch /usr/local/Modules/applications/root/6.04.14')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/root/6.04.14')
			node.ssh.execute('echo "set root /opt/software/root/root-6.04.14" >> /usr/local/Modules/applications/root/6.04.14')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/root/6.04.14')
