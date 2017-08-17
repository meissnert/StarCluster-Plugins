from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class VCFToolsInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing vcftools 0.1.12b on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/vcftools http://sourceforge.net/projects/vcftools/files/vcftools_0.1.12b.tar.gz')
			node.ssh.execute('tar xvzf /opt/software/vcftools/vcftools_0.1.12b.tar.gz -C /opt/software/vcftools/')
			node.ssh.execute('cd /opt/software/vcftools/vcftools_0.1.12b && make')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/vcftools/;touch /usr/local/Modules/applications/vcftools/0.1.12b')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/vcftools/0.1.12b')
			node.ssh.execute('echo "set root /opt/software/vcftools/vcftools_0.1.12b" >> /usr/local/Modules/applications/vcftools/0.1.12b')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/vcftools/0.1.12b')
			node.ssh.execute('echo -e "prepend-path\tPERL5LIB\t/opt/software/vcftools/vcftools_0.1.12b/perl/" >> /usr/local/Modules/applications/vcftools/0.1.12b')