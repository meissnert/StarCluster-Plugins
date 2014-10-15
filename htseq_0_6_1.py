from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class HTSeqInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing HTSeq 0.6.1 on %s" % (node.alias))
			log.info("...installing dependencies")
			node.ssh.execute('apt-get install -y build-essential python2.7-dev python-numpy python-matplotlib')
			log.info("...dependencies installed --> downloading HTSeq")
			node.ssh.execute('wget -c -P /opt/software/htseq https://pypi.python.org/packages/source/H/HTSeq/HTSeq-0.6.1.tar.gz')
			log.info("...HTSeq has downloaded --> decompressing files")
			node.ssh.execute('tar xvzf /opt/software/htseq/HTSeq-0.6.1.tar.gz -C /opt/software/htseq')
			log.info("...files decompressed --> running install scripts")
			node.ssh.execute('cd /opt/software/htseq/HTSeq-0.6.1 && python setup.py build && python setup.py install')