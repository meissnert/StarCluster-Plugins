from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SystemInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Updating the system on %s " % (node.alias))
			node.ssh.execute('echo "deb http://archive.canonical.com/ubuntu trusty partner" >> /etc/apt/sources.list')
			node.ssh.execute('echo "deb-src http://archive.canonical.com/ubuntu trusty partner" >> /etc/apt/sources.list')
			node.ssh.execute('apt-get -y update')
			node.ssh.execute('DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade')
			#node.ssh.execute("DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::='--force-confdef' -o Dpkg::Options::='--force-confold' install linux-image-extra-`uname -r | sed 's/^\(.\{7\}\)./\1/' | sed 's/^\(.\{9\}\)./\1/' | sed 's/^\(.\{9\}\)./\1/' | sed 's/^\(.\{9\}\)./\1/'`")
			node.ssh.execute('mkdir Downloads')
			node.ssh.execute('mkdir -p /opt/software')

			log.info("Installing Docker on %s " % (node.alias))
			node.ssh.execute('apt-get -y install docker.io')
			node.ssh.execute('ln -sf /usr/bin/docker.io /usr/local/bin/docker')
			node.ssh.execute("sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io")
			node.ssh.execute('update-rc.d docker.io defaults')

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
			node.ssh.execute('pip install s3cmd')

			log.info("Installing lvm2 on %s " % (node.alias))
			node.ssh.execute('apt-get -y install lvm2')

			log.info("Installing xfs on %s " % (node.alias))
			node.ssh.execute('apt-get -y install xfsdump xfslibs-dev xfsprogs')

			log.info("Installing pigz on %s " % (node.alias))
			node.ssh.execute('apt-get -y install pigz')
			node.ssh.execute('apt-get -y install libjemalloc-dev libbz2-dev libsnappy-dev')

			log.info("Installing qmem script on %s " % (node.alias))
			node.ssh.execute('wget -c -P Downloads https://raw.githubusercontent.com/txemaheredia/qmem/master/qmem')
			node.ssh.execute('chmod +x Downloads/qmem')
			node.ssh.execute('cp Downloads/qmem /usr/bin')

			log.info("Installing GeneTorrent on %s" % (node.alias))
			node.ssh.execute('apt-get -y install libboost-filesystem1.54.0 libboost-program-options1.54.0 libboost-regex1.54.0 libxerces-c3.1 libxqilla6')
			node.ssh.execute('wget -c -P Downloads https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.7/genetorrent-common_3.8.7-ubuntu2.207-14.04_amd64.deb')
			node.ssh.execute('wget -c -P Downloads https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.7/genetorrent-download_3.8.7-ubuntu2.207-14.04_amd64.deb')
			node.ssh.execute('dpkg -i ~/Downloads/genetorrent-common_3.8.7-ubuntu2.207-14.04_amd64.deb ~/Downloads/genetorrent-download_3.8.7-ubuntu2.207-14.04_amd64.deb')
			node.ssh.execute('apt-get -u install -f')

			log.info("Installing s3fs on %s" % (node.alias))
			node.ssh.execute('apt-get install -y build-essential git libfuse-dev libcurl4-openssl-dev libxml2-dev mime-support automake libtool')
			node.ssh.execute('apt-get install -y pkg-config libssl-dev')
			node.ssh.execute('cd /opt/software && git clone https://github.com/s3fs-fuse/s3fs-fuse.git')
			node.ssh.execute('cd /opt/software/s3fs-fuse && autoreconf --install && ./configure --prefix=/usr --with-openssl')
			node.ssh.execute('cd /opt/software/s3fs-fuse && make && make install')

			log.info("Installing ya3fs on %s" % (node.alias))
			node.ssh.execute('apt-get -y install fuse python-pip')
			node.ssh.execute('pip install yas3fs')
			node.ssh.execute("sed -i'' 's/^# *user_allow_other/user_allow_other/' /etc/fuse.conf")
			node.ssh.execute('chmod a+r /etc/fuse.conf')

			log.info("Installing additional system tools...")
			node.ssh.execute('apt-get install -y tcl tcl-dev tabix aria2 moreutils zip cmake libhdf5-dev')
			
			log.info("Installing python modules")
			node.ssh.execute('pip install pysam')
			node.ssh.execute('pip install networkx')
			node.ssh.execute('pip install deeptools')

			log.info("Installing Illumina BaseMount")
			node.ssh.execute('wget -c -P Downloads https://bintray.com/artifact/download/basespace/BaseSpaceFS-DEB/bsfs_1.1.631-1_amd64.deb')
			node.ssh.execute('wget -c -P Downloads https://bintray.com/artifact/download/basespace/BaseMount-DEB/basemount_0.1.2.463-20150714_amd64.deb')
			node.ssh.execute('sudo dpkg -i --force-confmiss ~/Downloads/bsfs_1.1.631-1_amd64.deb')
			node.ssh.execute('sudo dpkg -i ~/Downloads/basemount_0.1.2.463-20150714_amd64.deb')

			# link sh to bash, instead of dash
			node.ssh.execute('mv /bin/sh /bin/sh.orig')
			node.ssh.execute('ln -s /bin/bash /bin/sh')

			log.info("Installing Ganglia monitoring")
			master.ssh.execute('export DEBIAN_FRONTEND=noninteractive && apt-get install -y ganglia-monitor rrdtool gmetad ganglia-webfrontend')

			log.info("Installing jupyter")
			node.ssh.execute('apt-get -y install npm nodejs-legacy')
			node.ssh.execute('npm install -g configurable-http-proxy')
			node.ssh.execute('apt-get -y install python3-pip')
			node.ssh.execute('pip3 install jupyterhub')

			log.info('Fix ssh timeout')
			node.ssh.execute('echo ClientAliveInterval 60 >> /etc/ssh/sshd_config && service ssh restart')

			log.info('Clean up...')
			node.ssh.execute('rm -rvf /tmp/*')
			node.ssh.execute('apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && apt-get autoclean && apt-get autoremove -y')



