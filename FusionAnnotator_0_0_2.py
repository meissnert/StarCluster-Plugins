from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class FusionAnnotatorInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing FusionAnnotator 0.0.2 on %s " % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/fusionannotator')
			node.ssh.execute('wget -c -P /opt/software/fusionannotator https://github.com/FusionAnnotator/FusionAnnotator/archive/v0.0.2.tar.gz')
			node.ssh.execute('tar -zxf /opt/software/fusionannotator/v0.0.2.tar.gz -C /opt/software/fusionannotator/')
			node.ssh.execute('make -C /opt/software/fusionannotator/FusionAnnotator-0.0.2')
                        node.ssh.execute('cd /opt/software/fusionannotator/FusionAnnotator-0.0.2/RESOURCES && tar -zxf Hg19_CTAT_fusion_annotator_lib.tar.gz')

			node.ssh.execute('mkdir -p /usr/local/Modules/applications/fusionannotator/;touch /usr/local/Modules/applications/fusionannotator/0.0.2')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/fusionannotator/0.0.2')
			node.ssh.execute('echo "set root /opt/software/fusionannotator/FusionAnnotator-0.0.2" >> /usr/local/Modules/applications/fusionannotator/0.0.2')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/fusionannotator/0.0.2')
