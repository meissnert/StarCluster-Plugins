from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class FusionCatcherInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing FusionCatcher 0.99.3c on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/fusioncatcher http://sourceforge.net/projects/fusioncatcher/files/fusioncatcher_v0.99.3c.zip')
			node.ssh.execute('unzip /opt/software/fusioncatcher/fusioncatcher_v0.99.3c.zip -d /opt/software/fusioncatcher')
			node.ssh.execute('apt-get install -y python-biopython python-openpyxl python-xlrd python-dev zlib1g-dev')
			node.ssh.execute('module load ucsc-tools')
			node.ssh.execute('module load bowtie/1.0.1')
			node.ssh.execute('module load sra-toolkit/2.4.1')
			node.ssh.execute('module load samtools/0.1.19')
			node.ssh.execute('module load star/2.4.0d')

			node.ssh.execute('cd /opt/software/fusioncatcher/fusioncatcher_v0.99.3c && python bootstrap.py -y --prefix=/opt/software/fusioncatcher/v0.99.3c')
			node.ssh.execute('mkdir -p /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data')
			#node.ssh.execute('ln -s /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/fusioncatcher/;touch /usr/local/Modules/applications/fusioncatcher/0.99.3c')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/fusioncatcher/0.99.3c')
			node.ssh.execute('echo "module load ucsc-tools" >> /usr/local/Modules/applications/fusioncatcher/0.99.3c')
			node.ssh.execute('echo "module load samtools/0.1.19" >> /usr/local/Modules/applications/fusioncatcher/0.99.3c')
			node.ssh.execute('echo "set root /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/" >> /usr/local/Modules/applications/fusioncatcher/0.99.3c')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/fusioncatcher/0.99.3c')
