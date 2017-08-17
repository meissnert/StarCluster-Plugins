from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class STARInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing STAR 2.4.2a on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/star https://github.com/alexdobin/STAR/archive/STAR_2.4.2a.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/star/STAR_2.4.2a.tar.gz -C /opt/software/star')
			node.ssh.execute('make STAR -C /opt/software/star/STAR-STAR_2.4.2a/source')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/star/;touch /usr/local/Modules/applications/star/2.4.2a')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/star/2.4.2a')
			node.ssh.execute('echo "set root /opt/software/star/STAR-STAR_2.4.2a" >> /usr/local/Modules/applications/star/2.4.2a')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/source" >> /usr/local/Modules/applications/star/2.4.2a')