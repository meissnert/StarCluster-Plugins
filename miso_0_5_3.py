from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class MisoInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing MISO 0.5.3 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/miso/0.5.3 http://pypi.python.org/packages/source/m/misopy/misopy-0.5.3.tar.gz')
			node.ssh.execute('cd /opt/software/miso/0.5.3 && tar xzf misopy-0.5.3.tar.gz')
			node.ssh.execute('cd /opt/software/miso/0.5.3/misopy-0.5.3 && python setup.py build')
			node.ssh.execute('cd /opt/software/miso/0.5.3/misopy-0.5.3 && python setup.py install')
			node.ssh.execute('chmod +x /opt/software/miso/0.5.3/misopy-0.5.3/misopy/*.py')
			
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/miso/;touch /usr/local/Modules/applications/miso/0.5.3')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/miso/0.5.3')
			node.ssh.execute('echo "set root /opt/software/miso/0.5.3/misopy-0.5.3" >> /usr/local/Modules/applications/miso/0.5.3')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/misopy" >> /usr/local/Modules/applications/miso/0.5.3')
			
