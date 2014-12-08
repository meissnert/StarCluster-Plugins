from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class Setup(ClusterSetup):
    def run(self, nodes, master, user, user_shell, volumes):
        for node in nodes:
            # set fusioncatcher symlink
            node.ssh.execute('ln -s -f /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')
            
            # set intogen symlink
            node.ssh.execute('ln -s -f /data/database/intogen /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/data')

    def on_add_node(self, node, nodes, master, user, user_shell, volumes):
        # set fusioncatchdr symlink
        node.ssh.execute('ln -s -f /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')

        # set intogen symlinks
        node.ssh.execute('ln -s -f /data/database/intogen /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/data')

        # add manually mounted storage
        #host = master.ssh.execute('cat /etc/hosts | tail -n 1 | cut -f 2 -d " "')[1]
        master.ssh.execute('echo "/data/storage" %s"(async,no_root_squash,no_subtree_check,rw)" >> /etc/exports' % (node.alias))
        master.ssh.execute('exportfs -a')
        node.ssh.execute('mkdir -p /data/storage')
        node.ssh.execute('if mount | grep /data/storage; then echo "already mounted"; else mount -t nfs master:/data/storage /data/storage; fi')
        # node.ssh.execute('mount -t nfs master:/data/storage /data/storage')

        # add manually mounted s3 basespacebackup bucket
        master.ssh.execute('echo "/data/s3/basespacebackup" %s"(async,no_root_squash,no_subtree_check,rw,fsid=0)" >> /etc/exports' % (node.alias))
        master.ssh.execute("awk '!a[$0]++' /etc/exports | sponge /etc/exports") # get rid of duplicate entries 
        master.ssh.execute('exportfs -a')
        node.ssh.execute('mkdir -p /data/s3/basespacebackup')
        node.ssh.execute('if mount | grep /data/s3/basespacebackup; then echo "already mounted"; else mount -t nfs master:/data/s3/basespacebackup /data/s3/basespacebackup; fi')

        # add authorized users for passwordless ssh login
        # master.ssh.execute('for i in $(ls /home); do scp /home/$i/.ssh/authorized_keys %s:/home/$i/.ssh; done' % (node.alias))
        # master.ssh.execute('for i in $(ls /home); do scp /home/$i/.ssh/id_rsa.pub %s:/home/$i/.ssh; done' % (node.alias))
        # master.ssh.execute('for i in $(ls /home); do scp /home/$i/.ssh/id_rsa %s:/home/$i/.ssh; done' % (node.alias))

        # sync node with headnode
        log.info('Syncing software with master node...')
        master.ssh.execute('rsync -avzh /opt/software/ %s:/opt/software/' % (node.alias))
        master.ssh.execute('rsync -avzh /usr/local/Modules/applications/ %s:/usr/local/Modules/applications/' % (node.alias))

        node.ssh.execute('mv /bin/sh /bin/sh.orig')
        node.ssh.execute('ln -s /bin/bash /bin/sh')

        # install ganglia monitoring
        log.info("Install Ganglia monitoring")
        master.ssh.execute('scp /gmond.conf %s:/etc/ganglia/gmond.conf' % (node.alias))
        node.ssh.execute('service ganglia-monitor restart')
