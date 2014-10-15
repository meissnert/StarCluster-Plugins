from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class Setup(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			# set fusioncatcher symlink
			node.ssh.execute('ln -s /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')

        def on_add_node(self, node, nodes, master, user, user_shell, volumes):
        	# set fusioncatchdr symlink
        	node.ssh.execute('ln -s /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')

        	# set intogen symlink
        	node.ssh.execute('ln -s /data/database/intogen /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/data')