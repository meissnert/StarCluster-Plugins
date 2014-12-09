from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class seqtkInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing seqtk 1.0 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/seqtk/ https://github.com/lh3/seqtk/archive/1.0.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/seqtk/1.0.tar.gz -C /opt/software/seqtk')
			node.ssh.execute('cd /opt/software/seqtk/seqtk-1.0 && make')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/seqtk/;touch /usr/local/Modules/applications/seqtk/1.0')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/seqtk/1.0')
			node.ssh.execute('echo "set root /opt/software/seqtk/seqtk-1.0" >> /usr/local/Modules/applications/seqtk/1.0')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/seqtk/1.0')
