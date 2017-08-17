from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class kallistoInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Kallisto 0.42.2.1 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/kallisto')
			node.ssh.execute('wget -c -P /opt/software/kallisto https://github.com/pachterlab/kallisto/archive/v0.42.2.1.tar.gz')
			node.ssh.execute('tar -xzf /opt/software/kallisto/v0.42.2.1.tar.gz -C /opt/software/kallisto')
			node.ssh.execute('apt-get update')
			node.ssh.execute('apt-get -y install libhdf5-dev')
			node.ssh.execute('apt-get -y install zlib1g-dev')
			node.ssh.execute('cd /opt/software/kallisto/kallisto-0.42.2.1 && ./gen_release.sh linux')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/kallisto/;touch /usr/local/Modules/applications/kallisto/0.42.2.1')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/kallisto/0.42.2.1')
			node.ssh.execute('echo "set root /opt/software/kallisto/kallisto-0.42.2.1" >> /usr/local/Modules/applications/kallisto/0.42.2.1')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/release/kallisto" >> /usr/local/Modules/applications/kallisto/0.42.2.1')
