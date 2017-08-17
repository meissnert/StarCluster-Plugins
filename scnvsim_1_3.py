from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SCNVSimInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing SCNVSim 1.3 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/scnvsim http://downloads.sourceforge.net/project/scnvsim/scnvsim_1_3.zip')
			node.ssh.execute('unzip -d /opt/software/scnvsim /opt/software/scnvsim/scnvsim_1_3.zip')
			node.ssh.execute('chmod +x /opt/software/scnvsim/scnvsim_1_3/*.jar')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/scnvsim/;touch /usr/local/Modules/applications/scnvsim/1.3')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/scnvsim/1.3')
			node.ssh.execute('echo "set root /opt/software/scnvsim/scnvsim_1_3" >> /usr/local/Modules/applications/scnvsim/1.3')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/scnvsim/1.3')