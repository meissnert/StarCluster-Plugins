from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class FakeModInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Creating python 2.6.5 module files on %s" % (node.alias))
			node.ssh.execute('mkdir /usr/local/Modules/applications/python')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/python/2.6.5')
			node.ssh.execute('echo "set root /usr/bin/python" >> /usr/local/Modules/applications/python/2.6.5')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/python/2.6.5')

			log.info("Creating python 2.7.4 module files on %s" % (node.alias))
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/python/2.7.4')
			node.ssh.execute('echo "set root /usr/bin/python" >> /usr/local/Modules/applications/python/2.7.4')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/python/2.7.4')

			log.info("Creating GATK 3.2-2 module files on %s" % (node.alias))
			node.ssh.execute('mkdir /usr/local/Modules/applications/gatk')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/gatk/3.2-2')
			node.ssh.execute('echo "set root /opt/software/gatk/3.2-2" >> /usr/local/Modules/applications/gatk/3.2-2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/gatk/3.2-2')			
			node.ssh.execute('mkdir -p /opt/software/gatk/3.2-2')
			
			log.info("Creating MuTect 1.1.4 module files on %s" % (node.alias))
			node.ssh.execute('mkdir /usr/local/Modules/applications/mutect')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/mutect/1.1.4')
			node.ssh.execute('echo "set root /opt/software/mutect/1.1.4" >> /usr/local/Modules/applications/mutect/1.1.4')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/mutect/1.1.4')
			node.ssh.execute('mkdir -p /opt/software/mutect/1.1.4')
