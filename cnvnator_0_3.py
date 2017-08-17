from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class CNVnatorInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing CNVnator 0.3 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/cnvnator http://sv.gersteinlab.org/cnvnator/CNVnator_v0.3.zip')
			node.ssh.execute('unzip /opt/software/cnvnator/CNVnator_v0.3.zip -d /opt/software/cnvnator')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/cnvnator/;touch /usr/local/Modules/applications/cnvnator/0.3')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/cnvnator/0.3')
			node.ssh.execute('echo "set root /opt/software/cnvnator/CNVnator_v0.3" >> /usr/local/Modules/applications/cnvnator/0.3')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/cnvnator/0.3')
