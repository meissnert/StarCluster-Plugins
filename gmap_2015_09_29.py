from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class GMAPInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing GMAP-GSNAP 2015-09-29 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/gmap http://research-pub.gene.com/gmap/src/gmap-gsnap-2015-09-29.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/gmap/gmap-gsnap-2015-09-29.tar.gz -C /opt/software/gmap')
			node.ssh.execute('cd /opt/software/gmap/gmap-2015-09-29 && ./configure --prefix=/opt/software/gmap/gmap-2015-09-29/ --with-gmapdb=/data/database/gmapdb')
			node.ssh.execute('cd /opt/software/gmap/gmap-2015-09-29 && make')
			node.ssh.execute('cd /opt/software/gmap/gmap-2015-09-29 && make install')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/gmap/;touch /usr/local/Modules/applications/gmap/2015-09-29')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/gmap/2015-09-29')
			node.ssh.execute('echo "set root /opt/software/gmap/gmap-2015-09-29" >> /usr/local/Modules/applications/gmap/2015-09-29')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/gmap/2015-09-29')