from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BedtoolsInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Bedtools 2.21 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/bedtools https://github.com/arq5x/bedtools2/releases/download/v2.21.0/bedtools-2.21.0.tar.gz')
			node.ssh.execute('tar -xvzf /opt/software/bedtools/bedtools-2.21.0.tar.gz -C /opt/software/bedtools/')
			node.ssh.execute('mv /opt/software/bedtools/bedtools2 /opt/software/bedtools/bedtools2.21')
			node.ssh.execute('make -C /opt/software/bedtools/bedtools2.21')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/bedtools/;touch /usr/local/Modules/applications/bedtools/2.21')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/bedtools/2.21')
			node.ssh.execute('echo "set root /opt/software/bedtools/bedtools2.21" >> /usr/local/Modules/applications/bedtools/2.21')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/bedtools/2.21')