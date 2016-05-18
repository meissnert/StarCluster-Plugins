from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class CNVnatorInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing CNVnator 0.3.2 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/cnvnator https://github.com/abyzovlab/CNVnator/releases/download/v0.3.2/CNVnator_v0.3.2.zip')
			node.ssh.execute('unzip /opt/software/cnvnator/CNVnator_v0.3.2.zip -d /opt/software/cnvnator')
			node.ssh.execute('cd /opt/software/cnvnator/CNVnator_v0.3.2/src/samtools && make')
			node.ssh.execute('export ROOTSYS=/opt/software/root/root-6.04.14')
			node.ssh.execute('export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${ROOTSYS}/lib')
			node.ssh.execute('source /opt/software/root/root-6.04.14/bin/thisroot.sh')
			node.ssh.execute('cd /opt/software/cnvnator/CNVnator_v0.3.2/src && make OMP=no')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/cnvnator/;touch /usr/local/Modules/applications/cnvnator/0.3.2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/cnvnator/0.3.2')
			node.ssh.execute('echo "set root /opt/software/cnvnator/CNVnator_v0.3.2" >> /usr/local/Modules/applications/cnvnator/0.3.2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/cnvnator/0.3.2')
