from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class VarDictInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing VarDcit 1.4.5 on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/vardict')
			node.ssh.execute('cd /opt/software/vardict && git clone --recursive https://github.com/AstraZeneca-NGS/VarDictJava.git')
			node.ssh.execute('cd /opt/software/vardict &&  ./gradlew clean installApp')
                        node.ssh.execute('cd /opt/software/vardict &&  ./gradlew clean javadoc')
                        node.ssh.execute('cd /opt/software/vardict/VarDictJava/dist/ &&  unzip VarDict-1.4.5.zip')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/vardict/;touch /usr/local/Modules/applications/vardict/1.4.5')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/vardict/1.4.5')
			node.ssh.execute('echo "set root /opt/software/vardict" >> /usr/local/Modules/applications/vardict/1.4.5')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/vardict/1.4.5')
