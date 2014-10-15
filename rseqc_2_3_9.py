from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class RSeQCInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing RSeQC 2.3.9 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/rseqc http://sourceforge.net/projects/rseqc/files/RSeQC-2.3.9.tar.gz')
			node.ssh.execute('tar xvzf /opt/software/rseqc/RSeQC-2.3.9.tar.gz -C /opt/software/rseqc')
			node.ssh.execute('mkdir -p /opt/software/rseqc/RSeQC-2.3.9/lib/python2.7/site-packages/')
			node.ssh.execute('export PYTHONPATH=/opt/software/rseqc/RSeQC-2.3.9/lib/python2.7/site-packages && cd /opt/software/rseqc/RSeQC-2.3.9 && python setup.py install --prefix=/opt/software/rseqc/RSeQC-2.3.9')		
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/rseqc/;touch /usr/local/Modules/applications/rseqc/2.3.9')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/rseqc/2.3.9')
			node.ssh.execute('echo "set root /opt/software/rseqc/RSeQC-2.3.9" >> /usr/local/Modules/applications/rseqc/2.3.9')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/rseqc/2.3.9')
			node.ssh.execute('echo -e "prepend-path\tPYTHONPATH\t\$root/lib/python2.7/site-packages" >> /usr/local/Modules/applications/rseqc/2.3.9')
