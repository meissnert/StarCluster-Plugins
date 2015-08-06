from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class CufflinksInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Cufflinks 2.2.1 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/cufflinks http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz')
			node.ssh.execute('tar xvzf /opt/software/cufflinks/cufflinks-2.2.1.Linux_x86_64.tar.gz -C /opt/software/cufflinks')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/cufflinks/;touch /usr/local/Modules/applications/cufflinks/2.2.1')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/cufflinks/2.2.1')
			node.ssh.execute('echo "set root /opt/software/cufflinks/cufflinks-2.2.1.Linux_x86_64" >> /usr/local/Modules/applications/cufflinks/2.2.1')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/cufflinks/2.2.1')