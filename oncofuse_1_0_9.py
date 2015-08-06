from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class OncoFuseInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Oncofuse 1.0.9b2 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/oncofuse')
			node.ssh.execute('wget -c -P /opt/software/oncofuse/ https://github.com/mikessh/oncofuse/releases/download/1.0.9b2/oncofuse-1.0.9b2.zip')
			node.ssh.execute('unzip /opt/software/oncofuse/oncofuse-1.0.9b2.zip -d /opt/software/oncofuse/')
			node.ssh.execute('chmod +x /opt/software/oncofuse/oncofuse-1.0.9b2/Oncofuse.jar')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/oncofuse/;touch /usr/local/Modules/applications/oncofuse/1.0.9b2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/oncofuse/1.0.9b2')
			node.ssh.execute('echo "set root /opt/software/oncofuse/oncofuse-1.0.9b2/" >> /usr/local/Modules/applications/oncofuse/1.0.9b2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/oncofuse/1.0.9b2')
