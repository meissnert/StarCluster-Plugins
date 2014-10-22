from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class Setup(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
		      # set fusioncatcher symlink
		      node.ssh.execute('ln -s -f /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')

		      # set intogen symlink
        	      node.ssh.execute('ln -s -f /data/database/intogen /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/data')

        def on_add_node(self, node, nodes, master, user, user_shell, volumes):
        	# set fusioncatchdr symlink
        	node.ssh.execute('ln -s -f /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')

        	# set intogen symlinks
        	node.ssh.execute('ln -s -f /data/database/intogen /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/data')

		# add manually mounted storage
                #host = master.ssh.execute('cat /etc/hosts | tail -n 1 | cut -f 2 -d " "')[1]
		master.ssh.execute('echo "/data/storage" %s"(async,no_root_squash,no_subtree_check,rw)" >> /etc/exports' % (node.alias))
		master.ssh.execute('exportfs -a')
		node.ssh.execute('mkdir -p /data/storage')
		node.ssh.execute('mount -t nfs master:/data/storage /data/storage')
