from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class OmicsPipeInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Docker on %s " % (node.alias))
			#node.ssh.execute('wget https://bitbucket.org/sulab/omics_pipe/downloads/apt_sources -O /etc/apt/sources.list')
			node.ssh.execute('apt-get -y update')
			node.ssh.execute('apt-get -y install linux-image-extra-`uname -r`')
			node.ssh.execute('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9')
			node.ssh.execute('echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list')
			node.ssh.execute('apt-get -y update')
			node.ssh.execute('apt-get -y install lxc-docker')

			log.info("Configuring perl locale on %s " % (node.alias))
			node.ssh.execute('locale-gen en_US en_US.UTF-8 hu_HU hu_HU.UTF-8')
			node.ssh.execute('dpkg-reconfigure locales')
			
			log.info("Installing Graphviz on %s " % (node.alias))
			node.ssh.execute('apt-get install -y graphviz')

			log.info("Installing mdadm on %s " % (node.alias))
			node.ssh.execute('export DEBIAN_FRONTEND=noninteractive && apt-get -q -y install mdadm --no-install-recommends')

			log.info("Installing s3cmd on %s " % (node.alias))
			node.ssh.execute('apt-get -y install s3cmd')

			log.info("Installing lvm2 on %s " % (node.alias))
			node.ssh.execute('apt-get -y install lvm2')

			log.info("Installing xfs on %s " % (node.alias))
			node.ssh.execute('apt-get -y install xfs xfsprogs')

			log.info("Installing pigz on %s " % (node.alias))
			node.ssh.execute('apt-get -y install pigz')
			node.ssh.execute('apt-get -y install libjemalloc-dev libbz2-dev libsnappy-dev')



			