from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class FREEBAYESInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing freebayes 0.9.21 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/freebayes')
			node.ssh.execute('cd /opt/software/freebayes && git clone --recursive git://github.com/ekg/freebayes.git')
			node.ssh.execute('cd /opt/software/freebayes/freebayes/ &&  git checkout v0.9.21 && git submodule update --recursive')
			node.ssh.execute('cd /opt/software/freebayes/freebayes/ && make')
			node.ssh.execute('mv /opt/software/freebayes/freebayes /opt/software/freebayes/freebayes_0.9.21')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/freebayes/;touch /usr/local/Modules/applications/freebayes/0.9.21')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/freebayes/0.9.21')
			node.ssh.execute('echo "set root /opt/software/freebayes/freebayes_0.9.21" >> /usr/local/Modules/applications/freebayes/0.9.21')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/freebayes/0.9.21')