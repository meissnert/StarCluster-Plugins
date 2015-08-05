from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class StrelkaInstaller(ClusterSetup):
        def run(self, nodes, master, user, user_shell, volumes):
                for node in nodes:
                        log.info("Installing Strelka 1.0.14 on %s " % (node.alias))
                        node.ssh.execute('mkdir -p /opt/software/strelka')
                        node.ssh.execute('wget -c -P /opt/software/strelka https://sites.google.com/site/strelkasomaticvariantcaller/home/download/strelka_workflow-1.0.14.tar.gz')
                        node.ssh.execute('tar -xvzf /opt/software/strelka/strelka_workflow-1.0.14.tar.gz -C /opt/software/strelka/')
			node.ssh.execute('mkdir -p /opt/software/strelka/1.0.14/')
			node.ssh.execute('cd /opt/software/strelka/strelka_workflow-1.0.14/ && ./configure --prefix=/opt/software/strelka/1.0.14/')
			node.ssh.execute('cd /opt/software/strelka/strelka_workflow-1.0.14/ && make')

                        node.ssh.execute('mkdir -p /usr/local/Modules/applications/strelka/;touch /usr/local/Modules/applications/strelka/1.0.14')
                        node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/strelka/1.0.14')
                        node.ssh.execute('echo "set root /opt/software/strelka/1.0.14" >> /usr/local/Modules/applications/strelka/1.0.14')
                        node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/strelka/1.0.14')
