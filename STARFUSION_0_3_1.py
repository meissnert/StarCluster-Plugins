from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class STARFUSIONInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing STAR-FUSION 0.3.1 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/star-fusion https://github.com/STAR-Fusion/STAR-Fusion/archive/v0.3.1.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/star-fusion/v0.3.1.tar.gz -C /opt/software/star-fusion')
			node.ssh.execute('cd /opt/software/star-fusion/STAR-Fusion-0.3.1 && make'

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/star-fusion/;touch /usr/local/Modules/applications/star-fusion/0.3.1')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/star-fusion/0.3.1')
			node.ssh.execute('echo "set root /opt/software/star-fusion/STAR-Fusion-0.3.1" >> /usr/local/Modules/applications/star-fusion/0.3.1')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/star-fusion/0.3.1')