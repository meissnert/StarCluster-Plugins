from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SNAPInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing SNAP 1.0 beta 13 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/snap http://snap.cs.berkeley.edu/downloads/snap-1.0beta.13-linux.tar.gz')
			node.ssh.execute('tar -xvzf /opt/software/snap/snap-1.0beta.13-linux.tar.gz -C /opt/software/snap')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/snap/;touch /usr/local/Modules/applications/snap/1.0.b13')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/snap/1.0.b13')
			node.ssh.execute('echo "set root /opt/software/snap/snap-1.0beta.13-linux" >> /usr/local/Modules/applications/snap/1.0.b13')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/snap/1.0.b13')

        def on_add_node(self, node, nodes, master, user, user_shell, volumes):
		log.info("Installing SNAP 1.0 beta 13 on %s" % (node.alias))
		node.ssh.execute('wget -c -P /opt/software/snap http://snap.cs.berkeley.edu/downloads/snap-1.0beta.13-linux.tar.gz')
		node.ssh.execute('tar -xvzf /opt/software/snap/snap-1.0beta.13-linux.tar.gz -C /opt/software/snap')

		node.ssh.execute('mkdir -p /usr/local/Modules/applications/snap/;touch /usr/local/Modules/applications/snap/1.0.b13')
		node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/snap/1.0.b13')
		node.ssh.execute('echo "set root /opt/software/snap/snap-1.0beta.13-linux" >> /usr/local/Modules/applications/snap/1.0.b13')
		node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/snap/1.0.b13')
