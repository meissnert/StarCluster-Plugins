from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class RInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing R 3.1.1 on %s" % (node.alias))
			log.info("...installing dependencies")
			node.ssh.execute('apt-get update')
			node.ssh.execute('apt-get install -y libreadline-dev ncurses-dev libpng-dev texinfo texlive texlive-base luatex texlive-latex-base texlive-luatex texlive-extra-utils texlive-latex-recommended texlive-fonts-extra freetype* libxml2 libxml2-dev libpng12-dev libcurl4-openssl-dev tk-dev xterm')
			node.ssh.execute('apt-get install -y libgtk2.0-dev xorg-dev')
			log.info("...dependencies installed --> --> downloading R")
			node.ssh.execute('wget -c -P /opt/software/R http://cran.us.r-project.org/src/base/R-3/R-3.1.1.tar.gz')
			log.info("...R has downloaded --> decompressing files")
			node.ssh.execute('tar xvzf /opt/software/R/R-3.1.1.tar.gz -C /opt/software/R')
			log.info("...files decompressed --> running ./configure")
			node.ssh.execute('cd /opt/software/R/R-3.1.1 && ./configure --with-lapack --with-blas --with-pic --enable-threads --with-x=yes --enable-R-shlib --with-libpng --with-jpeglib --with-recommended-packages=yes')
			log.info("...configure has finished --> running make")
			node.ssh.execute('make -C /opt/software/R/R-3.1.1')
			log.info("...make has finished --> creating modulefiles")

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/R/;touch /usr/local/Modules/applications/R/3.1.1')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/R/3.1.1')
			node.ssh.execute('echo "set root /opt/software/R/R-3.1.1" >> /usr/local/Modules/applications/R/3.1.1')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/R/3.1.1')

			log.info("...installing R packages")
			log.info("...installing packages from CRAN")

			node.ssh.execute('wget -c -P /opt/software/R https://bitbucket.org/sulab/omics_pipe/raw/e345e666dd70711f79d310fe451a361893626196/dist/AWS_customBuild/Rprofile')
			node.ssh.execute('cp /opt/software/R/Rprofile ~/.Rprofile')
			node.ssh.execute('wget -c -P /opt/software/R https://bitbucket.org/sulab/omics_pipe/raw/e345e666dd70711f79d310fe451a361893626196/dist/AWS_customBuild/packages_cran.R')
			node.ssh.execute('wget -c -P /opt/software/R https://bitbucket.org/sulab/omics_pipe/raw/e345e666dd70711f79d310fe451a361893626196/dist/AWS_customBuild/packages_bioc_1.R')
			node.ssh.execute('wget -c -P /opt/software/R https://bitbucket.org/sulab/omics_pipe/raw/e345e666dd70711f79d310fe451a361893626196/dist/AWS_customBuild/packages_bioc_2.R')
			
			node.ssh.execute('module load R/3.1.1 && Rscript /opt/software/R/packages_cran.R')
			log.info("...CRAN packages have been installed --> installing BioConductor packages")
			node.ssh.execute('module load R/3.1.1 && Rscript /opt/software/R/packages_bioc_1.R')
			log.info("...BioConductor1 packages have been installed")
			node.ssh.execute('module load R/3.1.1 && Rscript /opt/software/R/packages_bioc_2.R')
			log.info("...BioConductor2 packages have been installed")