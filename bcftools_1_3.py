from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BCFToolsInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing BCFTools 1.3 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/bcftools')
			node.ssh.execute('wget -c -P /opt/software/bcftools https://github.com/samtools/bcftools/releases/download/1.3/bcftools-1.3.tar.bz2')
			node.ssh.execute('tar -xvjpf /opt/software/bcftools/bcftools-1.3.tar.bz2 -C /opt/software/bcftools/')
			node.ssh.execute('make -C /opt/software/bcftools/bcftools-1.3')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/bcftools/;touch /usr/local/Modules/applications/bcftools/1.3')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/bcftools/1.3')
			node.ssh.execute('echo "set root /opt/software/bcftools/bcftools-1.3" >> /usr/local/Modules/applications/bcftools/1.3')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/bcftools/1.3')
