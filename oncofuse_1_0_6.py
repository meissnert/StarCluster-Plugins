from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class OncoFuseInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing Oncofuse 1.0.6 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/oncofuse')
			node.ssh.execute('wget -c -P /opt/software/oncofuse/ http://www.unav.es/genetica/oncofuse-v1.0.6.zip')
			node.ssh.execute('unzip /opt/software/oncofuse/oncofuse-v1.0.6.zip -d /opt/software/oncofuse/')
			node.ssh.execute('chmod +x /opt/software/oncofuse/oncofuse-v1.0.6/Oncofuse.jar')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/oncofuse/;touch /usr/local/Modules/applications/oncofuse/1.0.6')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/oncofuse/1.0.6')
			node.ssh.execute('echo "set root /opt/software/oncofuse/oncofuse-v1.0.6" >> /usr/local/Modules/applications/oncofuse/1.0.6')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/oncofuse/1.0.6')
