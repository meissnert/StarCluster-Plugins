from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SambambaInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing sambamba 0.4.7 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/sambamba')
			node.ssh.execute('wget -c -P /opt/software/sambamba/ https://github.com/lomereiter/sambamba/releases/download/v0.4.7/sambamba_v0.4.7_centos5.tar.bz2')
			node.ssh.execute('tar jxf /opt/software/sambamba/sambamba_v0.4.7_centos5.tar.bz2 -C /opt/software/sambamba')
			#node.ssh.execute('wget -c -P /opt/software/sambamba/ https://github.com/lomereiter/sambamba/archive/v0.4.7.tar.gz')
			#node.ssh.execute('tar xvzf /opt/software/sambamba/v0.4.7.tar.gz -C /opt/software/sambamba')
			#node.ssh.execute('wget -c -P /opt/software/sambamba/ http://launchpadlibrarian.net/77223383/libllvm2.7_2.7-6ubuntu4_amd64.deb')
			#node.ssh.execute('dpkg -i /opt/software/sambamba/libllvm2.7_2.7-6ubuntu4_amd64.deb')
			#mode.ssh.execute('wget http://master.dl.sourceforge.net/project/d-apt/files/d-apt.list -O /etc/apt/sources.list.d/d-apt.list')
			#node.ssh.execute('apt-get update && sudo apt-get -y --allow-unauthenticated install --reinstall d-apt-keyring && sudo apt-get update')
			#node.ssh.execute('apt-get -y install ldc gdc dmd-bin')
			#node.ssh.execute('make -C /opt/software/sambamba/sambamba-0.4.7')
			node.ssh.execute('cp /opt/software/sambamba/sambamba_v0.4.7 /opt/software/sambamba/sambamba')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/sambamba/;touch /usr/local/Modules/applications/sambamba/0.4.7')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/sambamba/0.4.7')
			node.ssh.execute('echo "set root /opt/software/sambamba" >> /usr/local/Modules/applications/sambamba/0.4.7')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/sambamba/0.4.7')
