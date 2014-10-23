from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class QC3Installer(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing QC3 1.22 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/qc3/1.22')
			node.ssh.execute('cd /opt/software/qc3/1.22 && git clone https://github.com/slzhao/QC3.git')
			node.ssh.execute('cd /opt/software/qc3/1.22/QC3 && git checkout e44b5a38d1544a862365cb319bb678773c2f254e')
			node.ssh.execute('chmod +x /opt/software/qc3/1.22/QC3/qc3.pl')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/qc3/;touch /usr/local/Modules/applications/qc3/1.22')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/qc3/1.22')
			node.ssh.execute('echo "set root /opt/software/qc3/1.22/QC3" >> /usr/local/Modules/applications/qc3/1.22')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/qc3/1.22')
			node.ssh.execute('echo module load R >> /usr/local/Modules/applications/qc3/1.22')
			node.ssh.execute('echo module load samtools >> /usr/local/Modules/applications/qc3/1.22')

        def on_add_node(self, node, nodes, master, user, user_shell, volumes):
		log.info("Installing QC3 1.22 on %s" % (node.alias))
		node.ssh.execute('mkdir -p /opt/software/qc3/1.22')
		node.ssh.execute('cd /opt/software/qc3/1.22 && git clone https://github.com/slzhao/QC3.git')
		node.ssh.execute('cd /opt/software/qc3/1.22/QC3 && git checkout e44b5a38d1544a862365cb319bb678773c2f254e')
		node.ssh.execute('chmod +x /opt/software/qc3/1.22/QC3/qc3.pl')

		node.ssh.execute('mkdir -p /usr/local/Modules/applications/qc3/;touch /usr/local/Modules/applications/qc3/1.22')
		node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/qc3/1.22')
		node.ssh.execute('echo "set root /opt/software/qc3/1.22/QC3" >> /usr/local/Modules/applications/qc3/1.22')
		node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/qc3/1.22')
		node.ssh.execute('echo module load R >> /usr/local/Modules/applications/qc3/1.22')
		node.ssh.execute('echo module load samtools >> /usr/local/Modules/applications/qc3/1.22')
