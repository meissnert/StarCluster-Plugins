from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class UCSCInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing UCSC-Tools 287 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/ucsc/287')
			#node.ssh.execute('wget -c -P /opt/software/ucsc/287 http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v287/blat/blat && chmod +x /opt/software/ucsc/287/blat')
			#node.ssh.execute('wget -c -P /opt/software/ucsc/287 http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v287/faToTwoBit && chmod +x /opt/software/ucsc/287/faToTwoBit')
			#node.ssh.execute('wget -c -P /opt/software/ucsc/287 http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v287/bedGraphToBigWig && chmod +x /opt/software/ucsc/287/bedGraphToBigWig')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/ucsc-tools/;touch /usr/local/Modules/applications/ucsc-tools/287')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/ucsc-tools/287')
			node.ssh.execute('echo "set root /opt/software/ucsc/287" >> /usr/local/Modules/applications/ucsc-tools/287')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/ucsc-tools/287')
