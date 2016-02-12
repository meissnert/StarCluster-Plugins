from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BreakdancerInstaller(ClusterSetup):
        def run(self, nodes, master, user, user_shell, volumes):
                for node in nodes:
                        log.info("Installing Breakdancer 1.1.2 on %s " % (node.alias))
                        node.ssh.execute('mkdir -p /opt/software/breakdancer')
                        node.ssh.execute('wget -c -P /opt/software/breakdancer https://sourceforge.net/projects/breakdancer/files/breakdancer-1.1.2_2013_03_08.zip')
                        node.ssh.execute('cd /opt/software/breakdancer/ && unzip breakdancer-1.1.2_2013_03_08.zip')

                        node.ssh.execute('mkdir -p /usr/local/Modules/applications/breakdancer/;touch /usr/local/Modules/applications/breakdancer/1.1.2')
                        node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/breakdancer/1.1.2')
                        node.ssh.execute('echo "set root /opt/software/breakdancer/breakdancer-1.1.2" >> /usr/local/Modules/applications/breakdancer/1.1.2')
                        node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/breakdancer/1.1.2')
