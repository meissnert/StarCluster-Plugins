from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class STARFUSIONInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing STAR-FUSION 1.1.0 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/star-fusion https://github.com/STAR-Fusion/STAR-Fusion/releases/download/v1.1.0/STAR-Fusion_v1.1.0.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/star-fusion/STAR-Fusion_v1.1.0.tar.gz -C /opt/software/star-fusion')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/star-fusion/;touch /usr/local/Modules/applications/star-fusion/1.1.0')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/star-fusion/1.1.0')
			node.ssh.execute('echo "set root /opt/software/star-fusion/STAR-Fusion_v1.1.0" >> /usr/local/Modules/applications/star-fusion/1.1.0')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/star-fusion/1.1.0')
