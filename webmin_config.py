from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class Webmin(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):			
		# install webmin
		log.info("Setting up webmin on the headnode")
		master.ssh.execute('sudo sh -c "echo deb http://download.webmin.com/download/repository sarge contrib > /etc/apt/sources.list.d/docker.list"')
		master.ssh.execute('sudo sh -c "wget -q http://www.webmin.com/jcameron-key.asc -O- | apt-key add -"')
		master.ssh.execute('sudo apt-get -y update')
		master.ssh.execute('sudo apt-get -y install webmin')
		master.ssh.execute('/usr/share/webmin/changepass.pl /etc/webmin/ root sulab') # set the password for the root user on webmin
