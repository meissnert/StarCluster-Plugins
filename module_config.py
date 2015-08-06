from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class ModuleInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing and setting up modules support on %s " % (node.alias))
			node.ssh.execute('wget -c -P Downloads http://downloads.sourceforge.net/project/modules/Modules/modules-3.2.10/modules-3.2.10.tar.gz')
			node.ssh.execute('tar xvzf Downloads/modules-3.2.10.tar.gz -C Downloads')
			node.ssh.execute('cd ~/Downloads/modules-3.2.10/ && CPPFLAGS="-DUSE_INTERP_ERRORLINE" ./configure')
			node.ssh.execute('cd ~/Downloads/modules-3.2.10 && make && make install')
			node.ssh.execute('cp /usr/local/Modules/3.2.10/init/sh /etc/profile.d/modules.sh')
			node.ssh.execute('chmod 755 /etc/profile.d/modules.sh')
			node.ssh.execute('. /etc/profile.d/modules.sh')	
			node.ssh.execute('echo "/usr/local/Modules/applications" >> ${MODULESHOME}/init/.modulespath')
			node.ssh.execute('echo ". /etc/profile.d/modules.sh" >> /etc/bash.bashrc')	
			node.ssh.execute('mkdir -p /usr/local/Modules/applications')		
