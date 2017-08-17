from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SystemInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Updating the system on %s " % (node.alias))
			#node.ssh.execute('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 16126D3A3E5C1192')
			#node.ssh.execute('wget -c https://help.ubuntu.com/12.04/sample/sources.list && cp sources.list /etc/apt/sources.list')
			node.ssh.execute('apt-get -y update')
			node.ssh.execute('DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade')
			node.ssh.execute('apt-get -y install linux-image-extra-`uname -r`')
			node.ssh.execute('mkdir Downloads')
			node.ssh.execute('mkdir -p /opt/software')

			log.info("Installing Docker on %s " % (node.alias))
			#node.ssh.execute('wget https://bitbucket.org/sulab/omics_pipe/downloads/apt_sources -O /etc/apt/sources.list')
			node.ssh.execute('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9')
			node.ssh.execute('echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list')
			node.ssh.execute('apt-get -y update')
			node.ssh.execute('apt-get -y install lxc-docker')

			log.info("Configuring perl locale on %s " % (node.alias))
			node.ssh.execute('locale-gen en_US en_US.UTF-8 hu_HU hu_HU.UTF-8')
			node.ssh.execute('dpkg-reconfigure locales')

			log.info("Installing PHP on %s " % (node.alias))
			node.ssh.execute('apt-get install -y php5')			

			log.info("Installing Java 1.7 on %s " % (node.alias))
			node.ssh.execute('apt-get install -y openjdk-7-jdk icedtea-7-plugin')
			node.ssh.execute('update-java-alternatives -s java-1.7.0-openjdk-amd64')		
			
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

			log.info("Installing qmem script on %s " % (node.alias))
			node.ssh.execute('wget -c -P Downloads https://raw.githubusercontent.com/txemaheredia/qmem/master/qmem')
			node.ssh.execute('chmod +x Downloads/qmem')
			node.ssh.execute('cp Downloads/qmem /usr/bin')

			log.info("Installing GeneTorrent on %s" % (node.alias))
			node.ssh.execute('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys D9CFF117BD794DCE7C080E310CFB84AE029DB5C7')
			node.ssh.execute('echo "deb http://ppa.launchpad.net/boost-latest/ppa/ubuntu precise main" >> /etc/apt/sources.list')
			node.ssh.execute('echo "deb-src http://ppa.launchpad.net/boost-latest/ppa/ubuntu precise main" >> /etc/apt/sources.list')
			node.ssh.execute('apt-get -y update')
			node.ssh.execute('apt-get -y install libboost-filesystem1.48.0 libboost-program-options1.48.0 libboost-regex1.48.0 libboost-system1.48.0 libxerces-c3.1 libxqilla6')
			#node.ssh.execute('wget -c https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.6/genetorrent-common_3.8.6-ubuntu2.130-12.04_amd64.deb')
			#node.ssh.execute('wget -c https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.6/genetorrent-download_3.8.6-ubuntu2.130-12.04_amd64.deb')
			#node.ssh.execute('dpkg -i genetorrent-common_3.8.6-ubuntu2.130-12.04_amd64.deb genetorrent-download_3.8.6-ubuntu2.130-12.04_amd64.deb')

			log.info("Installing s3fs on %s" % (node.alias))
			node.ssh.execute('apt-get install -y build-essential libfuse-dev fuse-utils libcurl4-openssl-dev libxml2-dev mime-support automake libtool')
			node.ssh.execute('cd /opt/software && git clone https://github.com/s3fs-fuse/s3fs-fuse.git')
			node.ssh.execute('cd /opt/software/s3fs-fuse && autoreconf --install && ./configure --prefix=/usr')
			node.ssh.execute('cd /opt/software/s3fs-fuse && make && make install')

			log.info("Installing ya3fs on %s" % (node.alias))
			node.ssh.execute('apt-get -y install fuse python-pip')
			node.ssh.execute('pip install yas3fs')
			node.ssh.execute("sed -i'' 's/^# *user_allow_other/user_allow_other/' /etc/fuse.conf")
			node.ssh.execute('chmod a+r /etc/fuse.conf')

			log.info("Installing additional system tools...")
			node.ssh.execute('apt-get install -y tcl tcl-dev tabix aria2 moreutils zip')

			# link sh to bash, instead of dash
			node.ssh.execute('mv /bin/sh /bin/sh.orig')
			node.ssh.execute('ln -s /bin/bash /bin/sh')

			log.info("Installing Ganglia monitoring")
			master.ssh.execute('export DEBIAN_FRONTEND=noninteractive && apt-get install -y ganglia-monitor rrdtool gmetad ganglia-webfrontend')

			log.info('Fix ssh timeout')
			node.ssh.execute('echo ClientAliveInterval 60 >> /etc/ssh/sshd_config && service ssh restart')
