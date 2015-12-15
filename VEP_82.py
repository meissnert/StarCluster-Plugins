from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class VEPInstaller(ClusterSetup):
        def run(self, nodes, master, user, user_shell, volumes):
                for node in nodes:
                        log.info("Installing VEP 82 on %s" % (node.alias))
                        node.ssh.execute('mkdir -p /opt/software/vep')
                        node.ssh.execute('cd /opt/software/vep && wget https://github.com/Ensembl/ensembl-tools/archive/release/82.zip')
                        node.ssh.execute('unzip -d /opt/software/vep /opt/software/vep/82.zip')
			node.ssh.execute('cd /opt/software/vep/ensembl-tools-release-82/scripts/variant_effect_predictor/ && perl INSTALL.pl -a ac -s homo_sapiens -y GRCh38')
                        node.ssh.execute('mv /opt/software/vep/ensembl-tools-release-82/ /opt/software/vep/vep_82')

                        node.ssh.execute('mkdir -p /usr/local/Modules/applications/vep/;touch /usr/local/Modules/applications/vep/82')
                        node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/vep/82')
                        node.ssh.execute('echo "set root /opt/software/vep/vep_82" >> /usr/local/Modules/applications/vep/82')
                        node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/vep/82')
