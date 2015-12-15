from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class PyVCFInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing PyVCF 0.6 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/pyvcf')
                        node.ssh.execute('pip install --target=d:\/opt/software/pyvcf pyvcf')
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/pyvcf/;touch /usr/local/Modules/applications/pyvcf/0.6')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/pyvcf/0.6')
			node.ssh.execute('echo "set root /opt/software/pyvcf/pyvcf-0.6" >> /usr/local/Modules/applications/pyvcf/0.6')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/pyvcf/0.6')
