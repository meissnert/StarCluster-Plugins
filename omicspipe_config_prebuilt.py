from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class OmicsPipeInstallerCL(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("installing omicspipe on the command line")
			node.ssh.execute('pip install -e hg+https://bitbucket.org/sulab/omics_pipe#egg=omics_pipe')

			log.info("pulling most recent omicspipe repository")
			node.ssh.execute('cd /omics_pipe && source /etc/environment && hg pull -b default')
			node.ssh.execute('cd /omics_pipe && source /etc/environment && hg update')

			log.info("updating apt-get sources list")
			node.ssh.execute('wget https://bitbucket.org/sulab/omics_pipe/downloads/apt_sources -O /etc/apt/sources.list')

        def on_add_node(self, node, nodes, master, user, user_shell, volumes):
                log.info("installing omicspipe on the command line")
                node.ssh.execute('pip install -e hg+https://bitbucket.org/sulab/omics_pipe#egg=omics_pipe')

                log.info("pulling most recent omicspipe repository")
                node.ssh.execute('cd /omics_pipe && source /etc/environment && hg pull -b default')
                node.ssh.execute('cd /omics_pipe && source /etc/environment && hg update')

                log.info("updating apt-get sources list")
                node.ssh.execute('wget https://bitbucket.org/sulab/omics_pipe/downloads/apt_sources -O /etc/apt/sources.list')

