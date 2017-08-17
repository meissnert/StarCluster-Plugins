from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class OmicsPipeInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Omics Pipe and dependencies on %s" % (node.alias))
			log.info("Installing Ruffus on %s" % (node.alias))
			node.ssh.execute('pip install ruffus --upgrade')

			log.info("Installing pyYAML on %s" % (node.alias))
			node.ssh.execute('pip install pyyaml')

			log.info("Installing Omics Pipe on %s" % (node.alias))
			node.ssh.execute('pip install -e hg+https://bitbucket.org/sulab/omics_pipe#egg=omics_pipe')