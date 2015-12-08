from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class R_3_2_2_Installer(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing R 3.2.2 on %s" % (node.alias))
			log.info("...installing dependencies")
			log.info("...dependencies installed --> --> downloading R")
			node.ssh.execute('wget -c -P /opt/software/R http://cran.us.r-project.org/src/base/R-3/R-3.2.2.tar.gz')
			log.info("...R has downloaded --> decompressing files")
			node.ssh.execute('tar xvzf /opt/software/R/R-3.2.2.tar.gz -C /opt/software/R')
			log.info("...files decompressed --> running ./configure")
			node.ssh.execute('cd /opt/software/R/R-3.2.2 && ./configure --with-lapack --with-blas --with-pic --enable-threads --with-x=yes --enable-R-shlib --with-libpng --with-jpeglib --with-recommended-packages=yes')
			log.info("...configure has finished --> running make")
			node.ssh.execute('make -C /opt/software/R/R-3.2.2')
			log.info("...make has finished --> creating modulefiles")

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/R/;touch /usr/local/Modules/applications/R/3.2.2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/R/3.2.2')
			node.ssh.execute('echo "set root /opt/software/R/R-3.2.2" >> /usr/local/Modules/applications/R/3.2.2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/R/3.2.2')
