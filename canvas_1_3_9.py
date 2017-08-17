from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class CanvasInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Canvas 1.3.9 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/canvas/1.3.9')
			node.ssh.execute('wget -c -P /opt/software/canvas/1.3.9 https://github.com/Illumina/canvas/releases/download/1.3.9/canvas-1.3.9_x64.zip')
			node.ssh.execute('cd /opt/software/canvas/1.3.9 && unzip canvas-1.3.9_x64.zip')
			node.ssh.execute('alias canvas="mono /opt/software/canvas/1.3.9/canvas-1.3.9_x64/Canvas.exe"')

#			log.info("Creating Canvas Module")
#			node.ssh.execute('mkdir -p /usr/local/Modules/applications/canvas/;touch /usr/local/Modules/applications/canvas/1.3.9')
#			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/canvas/1.3.9')
#			node.ssh.execute('echo "set root /opt/software/canvas/1.3.9" >> /usr/local/Modules/applications/canvas/1.3.9')
#			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/canvas/1.3.9')
