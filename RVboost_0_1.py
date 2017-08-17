from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class RVboostInstaller(ClusterSetup):
        def run(self, nodes, master, user, user_shell, volumes):
                for node in nodes:
                        log.info("Installing RVboost 0.1 on %s " % (node.alias))
                        node.ssh.execute('mkdir -p /opt/software/rvboost')
                        node.ssh.execute('wget -c -P /opt/software/rvboost http://bioinformaticstools.mayo.edu/research/wp-content/plugins/download.php?url=https://s3-us-west-2.amazonaws.com/mayo-bic-tools/rvboost/RVboost_0.1.tar.gz')
                        node.ssh.execute('tar -zxvf /opt/software/rvboost/download.php?url=https:%2F%2Fs3-us-west-2.amazonaws.com%2Fmayo-bic-tools%2Frvboost%2FRVboost_0.1.tar.gz -C /opt/software/rvboost/')
                        node.ssh.execute('mv /opt/software/rvboost/RVboost_0.1 /opt/software/rvboost/rvboost-0.1')
			node.ssh.execute('cd /opt/software/rvboost/rvboost-0.1 && ./setup.sh -r /data/database/GATK/hg19/ucsc.hg19.fasta')
                        node.ssh.execute('find /opt/software/rvboost/rvboost-0.1 -type d -exec chmod 755 {} +')

                        node.ssh.execute('mkdir -p /usr/local/Modules/applications/rvboost/;touch /usr/local/Modules/applications/rvboost/0.1')
                        node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/rvboost/0.1')
                        node.ssh.execute('echo "set root /opt/software/rvboost/rvboost-0.1" >> /usr/local/Modules/applications/rvboost/0.1')
                        node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/rvboost/0.1')
