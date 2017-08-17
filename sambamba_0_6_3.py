from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SambambaInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing sambamba 0.6.3 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/sambamba/0.6.3')
			node.ssh.execute('wget -c -P /opt/software/sambamba/ https://github.com/lomereiter/sambamba/releases/download/v0.6.3/sambamba_v0.6.3_linux.tar.bz2')
			node.ssh.execute('tar jxf /opt/software/sambamba/sambamba_v0.6.3_linux.tar.bz2 -C /opt/software/sambamba')
			node.ssh.execute('chmod +x /opt/software/sambamba/sambamba_v0.6.3')
			node.ssh.execute('cp /opt/software/sambamba/sambamba_v0.6.3 /opt/software/sambamba/0.6.3/sambamba')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/sambamba/;touch /usr/local/Modules/applications/sambamba/0.6.3')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/sambamba/0.6.3')
			node.ssh.execute('echo "set root /opt/software/sambamba/0.6.3" >> /usr/local/Modules/applications/sambamba/0.6.3')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/sambamba/0.6.3')
