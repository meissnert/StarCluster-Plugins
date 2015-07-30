from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SubreadInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Subread 1.4.6 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/subread/1.4.6 http://hivelocity.dl.sourceforge.net/project/subread/subread-1.4.6/subread-1.4.6-source.tar.gz')
			node.ssh.execute('tar xzf /opt/software/subread/1.4.6/subread-1.4.6-source.tar.gz')
			node.ssh.execute('cd /opt/software/subread/1.4.6/subread-1.4.6-source/src && make -f Makefile.Linux')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/subread/;touch /usr/local/Modules/applications/subread/1.4.6')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/subread/1.4.6')
			node.ssh.execute('echo "set root /opt/software/subread/1.4.6/subread-1.4.6-source" >> /usr/local/Modules/applications/subread/1.4.6')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/subread/1.4.6')
			
