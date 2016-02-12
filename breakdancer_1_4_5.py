from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class BreakdancerInstaller(ClusterSetup):
        def run(self, nodes, master, user, user_shell, volumes):
                for node in nodes:
                        log.info("Installing Breakdancer 1.4.5 on %s " % (node.alias))
                        node.ssh.execute('mkdir -p /opt/software/breakdancer')
			node.ssh.execute('cd /opt/software/breakdancer && git clone --recursive https://github.com/genome/breakdancer.git breakdancer_1_4_5')
			node.ssh.execute('cd /opt/software/breakdancer/breakdancer_1_4_5 && mkdir build')
			node.ssh.execute('cd /opt/software/breakdancer/breakdancer_1_4_5/build && cmake .. -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=/usr/local')
			node.ssh.execute('cd /opt/software/breakdancer/breakdancer_1_4_5/build && make')
			node.ssh.execute('cd /opt/software/breakdancer/breakdancer_1_4_5/build && make install')

	
                        node.ssh.execute('mkdir -p /usr/local/Modules/applications/breakdancer/;touch /usr/local/Modules/applications/breakdancer/1.4.5')
                        node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/breakdancer/1.4.5')
                        node.ssh.execute('echo "set root /opt/software/breakdancer/breakdancer_1_4_5" >> /usr/local/Modules/applications/breakdancer/1.4.5')
                        node.ssh.execute('echo -e "prepend-path\tPATH\t\$root" >> /usr/local/Modules/applications/breakdancer/1.4.5')
