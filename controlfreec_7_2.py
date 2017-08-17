from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class ControlFREECInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Control-FREEC 7.2 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/controlfreec/7.2 http://bioinfo-out.curie.fr/projects/freec/src/FREEC_Linux64.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/controlfreec/7.2/FREEC_Linux64.tar.gz -C /opt/software/controlfreec/7.2')
			node.ssh.execute('wget -c -P /opt/software/controlfreec/7.2 http://bioinfo-out.curie.fr/projects/freec/src/makeGraph.R')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/controlfreec/;touch /usr/local/Modules/applications/controlfreec/7.2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/controlfreec/7.2')
			node.ssh.execute('echo "set root /opt/software/controlfreec/7.2" >> /usr/local/Modules/applications/controlfreec/7.2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/controlfreec/7.2')
