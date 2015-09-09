from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class kallistoInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Kallisto git dev branch on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/kallisto')
			node.ssh.execute('apt-get update')
			node.ssh.execute('apt-get -y install libhdf5-dev')
			node.ssh.execute('apt-get -y install zlib1g-dev')
			node.ssh.execute('cd /opt/software/kallisto && git clone https://github.com/pachterlab/kallisto.git kallisto-dev -b devel')
			node.ssh.execute('cd /opt/software/kallisto/kallisto-dev && mkdir build')
			node.ssh.execute('cd /opt/software/kallisto/kallisto-dev/build && cmake ..')
			node.ssh.execute('cd /opt/software/kallisto/kallisto-dev/build && make')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/kallisto/;touch /usr/local/Modules/applications/kallisto/dev')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/kallisto/dev')
			node.ssh.execute('echo "set root /opt/software/kallisto/kallisto-dev" >> /usr/local/Modules/applications/kallisto/dev')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/build/src" >> /usr/local/Modules/applications/kallisto/dev')
