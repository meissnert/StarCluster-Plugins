from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class AGEInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing AGE 0.4 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/age/0.4')
			node.ssh.execute('wget -c -P /opt/software/age/0.4 https://github.com/marghoob/AGE/archive/simple-parseable-output.zip')
			node.ssh.execute('cd /opt/software/age/0.4 && unzip simple-parseable-output.zip')
			node.ssh.execute('cd /opt/software/age/0.4/AGE-simple-parseable-output && make OMP=no')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/age/;touch /usr/local/Modules/applications/age/0.4')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/age/0.4')
			node.ssh.execute('echo "set root /opt/software/age/0.4" >> /usr/local/Modules/applications/age/0.4')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/age/0.4')
