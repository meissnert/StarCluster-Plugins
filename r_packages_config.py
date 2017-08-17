from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class R_Packages(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):			
		# install R Packages
		log.info("Setting up R Packages")
		master.ssh.execute('module load R/3.1.0 && Rscript home/omicspipe/omics_pipe/dist/AWS_customBuild/packages.R')
