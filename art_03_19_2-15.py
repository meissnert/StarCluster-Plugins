from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class ARTInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing ART 03-19-2015 on %s" % (node.alias))
			node.ssh.execute('wget -c -P /opt/software/art/03192015 http://www.niehs.nih.gov/research/resources/assets/docs/artbinchocolatecherrycake031915linux64tgz.tgz')
			node.ssh.execute('tar -xvzf /opt/software/art/03192015/artbinchocolatecherrycake031915linux64tgz.tgz -C /opt/software/art/03192015')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/art/;touch /usr/local/Modules/applications/art/03192015')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/art/03192015')
			node.ssh.execute('echo "set root /opt/software/art/03192015" >> /usr/local/Modules/applications/art/03192015')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/art_bin_ChocolateCherryCake" >> /usr/local/Modules/applications/art/03192015')
