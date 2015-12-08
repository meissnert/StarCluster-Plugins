from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class MOJOInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing MOJO 0.0.5 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/mojo http://dmel.uchicago.edu/~chai/MOJO/releases/MOJO-v0.0.5-linux-x86_64.tar.gz')
			node.ssh.execute('tar zxf /opt/software/mojo/MOJO-v0.0.5-linux-x86_64.tar.gz -C /opt/software/mojo')

			node.ssh.execute('cp /opt/software/mojo/MOJO-v0.0.5-linux-x86_64/Sample.configfile.txt /opt/software/mojo/MOJO-v0.0.5-linux-x86_64/config.txt')
			node.ssh.execute("sed -i /opt/software/mojo/MOJO-v0.0.5-linux-x86_64/config.txt -e '5s/.*/mojo_install_dir = \/opt\/software\/mojo\/MOJO-v0.0.5-linux-x86_64\/bin\//'")
			node.ssh.execute("sed -i /opt/software/mojo/MOJO-v0.0.5-linux-x86_64/config.txt -e '6s/.*/mojo_reference_dir = \/data\/database\/mojo\/reference.hg19.Ensembl\//'")
			node.ssh.execute("sed -i /opt/software/mojo/MOJO-v0.0.5-linux-x86_64/config.txt -e '7s/.*/mojo_tools_dir = \/opt\/software\/mojo\/MOJO-v0.0.5-linux-x86_64\/external\//'")

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/mojo/;touch /usr/local/Modules/applications/mojo/0.0.5')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/mojo/0.0.5')
			node.ssh.execute('echo "set root /opt/software/mojo/MOJO-v0.0.5-linux-x86_64" >> /usr/local/Modules/applications/mojo/0.0.5')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/mojo/0.0.5')
			node.ssh.execute('echo -e "prepend-path\tLD_LIBRARY_PATH\t\$root/lib" >> /usr/local/Modules/applications/mojo/0.0.5')
