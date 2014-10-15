from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class QualiMapInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing QualiMap 2.0 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/qualimap http://qualimap.bioinfo.cipf.es/release/qualimap_v2.0.zip')
			node.ssh.execute('unzip -d /opt/software/qualimap /opt/software/qualimap/qualimap_v2.0.zip')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/qualimap/;touch /usr/local/Modules/applications/qualimap/2.0')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/qualimap/2.0')
			node.ssh.execute('echo "set root /opt/software/qualimap/qualimap_v2.0" >> /usr/local/Modules/applications/qualimap/2.0')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/qualimap/2.0')