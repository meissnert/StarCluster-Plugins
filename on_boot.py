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
        # master.ssh.execute('echo "/data/s3/basespacebackup" %s"(async,no_root_squash,no_subtree_check,rw,fsid=0)" >> /etc/exports' % (node.alias))
        # master.ssh.execute("awk '!a[$0]++' /etc/exports | sponge /etc/exports") # get rid of duplicate entries 
        # master.ssh.execute('exportfs -a')
        # node.ssh.execute('mkdir -p /data/s3/basespacebackup')
        # node.ssh.execute('if mount | grep /data/s3/basespacebackup; then echo "already mounted"; else mount -t nfs master:/data/s3/basespacebackup /data/s3/basespacebackup; fi')

        # master.ssh.execute('echo "/data/s3/averapatients" %s"(async,no_root_squash,no_subtree_check,rw,fsid=0)" >> /etc/exports' % (node.alias))
        # master.ssh.execute("awk '!a[$0]++' /etc/exports | sponge /etc/exports") # get rid of duplicate entries 
        # master.ssh.execute('exportfs -a')
        # node.ssh.execute('mkdir -p /data/s3/averapatients')
        # node.ssh.execute('if mount | grep /data/s3/averapatients; then echo "already mounted"; else mount -t nfs master:/data/s3/averapatients /data/s3/averapatients; fi')
        
        # master.ssh.execute('echo "/data/s3/averaprojects" %s"(async,no_root_squash,no_subtree_check,rw,fsid=0)" >> /etc/exports' % (node.alias))
        # master.ssh.execute("awk '!a[$0]++' /etc/exports | sponge /etc/exports") # get rid of duplicate entries 
        # master.ssh.execute('exportfs -a')
        # node.ssh.execute('mkdir -p /data/s3/averaprojects')
        # node.ssh.execute('if mount | grep /data/s3/averaprojects; then echo "already mounted"; else mount -t nfs master:/data/s3/averaprojects /data/s3/averaprojects; fi')

        # master.ssh.execute('echo "/data/s3/averafastq" %s"(async,no_root_squash,no_subtree_check,rw,fsid=0)" >> /etc/exports' % (node.alias))
        # master.ssh.execute("awk '!a[$0]++' /etc/exports | sponge /etc/exports") # get rid of duplicate entries 
        # master.ssh.execute('exportfs -a')
        # node.ssh.execute('mkdir -p /data/s3/averafastq')
        # node.ssh.execute('if mount | grep /data/s3/averafastq; then echo "already mounted"; else mount -t nfs master:/data/s3/averafastq /data/s3/averafastq; fi')

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

        # remount /tmp to /mnt/tmp
        log.info("Remounting /tmp to /mnt/tmp ..")
        node.ssh.execute('mkdir -p -m 1777 /mnt/tmp')
        node.ssh.execute('mount --bind /mnt/tmp /tmp')

        # mount s3 buckets
        log.info("Mounting S3 buckets ..")
        node.ssh.execute('mkdir -p /data/s3/basespacebackup')
        node.ssh.execute('mkdir -p /data/s3/averapatients')
        node.ssh.execute('mkdir -p /data/s3/averaprojects')
        node.ssh.execute('mkdir -p /data/s3/averafastq')

        node.ssh.execute('if mount | grep /data/s3/basespacebackup; then umount -l /data/s3/basespacebackup && s3fs averafastq /data/s3/basespacebackup -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs basespacebackup /data/s3/basespacebackup -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
        node.ssh.execute('if mount | grep /data/s3/averapatients; then umount -l /data/s3/averapatients && s3fs averapatients /data/s3/averapatients -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs averapatients /data/s3/averapatients -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
        node.ssh.execute('if mount | grep /data/s3/averaprojects; then umount -l /data/s3/averaprojects && s3fs averaprojects /data/s3/averaprojects -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs averaprojects /data/s3/averaprojects -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
        node.ssh.execute('if mount | grep /data/s3/averafastq; then umount -l /data/s3/averafastq && s3fs averafastq /data/s3/averafastq -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs averafastq /data/s3/averafastq -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
