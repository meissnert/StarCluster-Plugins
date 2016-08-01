
from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class Setup(ClusterSetup):
    def run(self, nodes, master, user, user_shell, volumes):
        for node in nodes:
            # set fusioncatcher symlink
            node.ssh.execute('ln -s -f /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')
            
            # set intogen symlink
            #node.ssh.execute('ln -s -f /data/database/intogen /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/data')

            #add cron job to clear out the s3fs cache that is older then 12 hours, run every minute
            node.ssh.execute("echo '* * * * * find /mnt/tmp/avera*/ -type f -mmin +$((60*12)) -exec rm -f '{}' \;' >> /var/spool/cron/crontabs/root")

    def on_add_node(self, node, nodes, master, user, user_shell, volumes):
        # set fusioncatchdr symlink
        node.ssh.execute('ln -s -f /databases/ensembl_v75 /opt/software/fusioncatcher/v0.99.3c/fusioncatcher/data/current')

        # set intogen symlinks
        #node.ssh.execute('ln -s -f /data/database/intogen /opt/software/intogen/intogen-mutations-analysis-7fbd0b4803be/data')

        # add manually mounted storage
        master.ssh.execute('echo "/data/storage" %s"(async,no_root_squash,no_subtree_check,rw)" >> /etc/exports' % (node.alias))
        master.ssh.execute('exportfs -a')
        node.ssh.execute('mkdir -p /data/storage')
        node.ssh.execute('if mount | grep /data/storage; then echo "already mounted"; else mount -t nfs master:/data/storage /data/storage; fi')

        #master.ssh.execute('echo "/data/basespace" %s"(async,no_root_squash,no_subtree_check,rw,fsid=0)" >> /etc/exports' % (node.alias))
        #master.ssh.execute('exportfs -a')
        #node.ssh.execute('if [ ! -d /data/basespace ]; then mkdir -p /data/basespace; fi')
        #node.ssh.execute('if mount | grep /data/basespace; then echo "already mounted"; else mount -t nfs master:/data/basespace /data/basespace; fi')        

        # sync node with headnode
        log.info('Syncing software with master node...')
        master.ssh.execute('rsync -avzh /opt/software/ %s:/opt/software/' % (node.alias))
        master.ssh.execute('rsync -avzh /usr/local/Modules/applications/ %s:/usr/local/Modules/applications/' % (node.alias))
        master.ssh.execute('rsync -avzh /usr/local/lib/ %s:/usr/local/lib/' % (node.alias))

        # set shell
        node.ssh.execute('mv /bin/sh /bin/sh.orig')
        node.ssh.execute('ln -s /bin/bash /bin/sh')

        # install ganglia monitoring
#        log.info("Install Ganglia monitoring")
#        master.ssh.execute('scp /etc/ganglia/gmond.conf %s:/etc/ganglia/gmond.conf' % (node.alias))
#        node.ssh.execute('service nginx stop')
#        node.ssh.execute('service ganglia-monitor restart && service gmetad restart && service apache2 restart')

        # remount /tmp to /mnt/tmp
        log.info('Remounting /tmp to /mnt/tmp ..')
        node.ssh.execute('mkdir -p -m 1777 /mnt/tmp')
        node.ssh.execute('mount --bind /mnt/tmp /tmp')

        # mount s3 buckets
        log.info("Mounting S3 buckets ..")
        #node.ssh.execute('mkdir -p /data/s3/basespacebackup')
        node.ssh.execute('mkdir -p /data/s3/averapatients')
        node.ssh.execute('mkdir -p /data/s3/averaprojects')
        node.ssh.execute('mkdir -p /data/s3/averafastq')
        node.ssh.execute('mkdir -p /data/s3/averamirt')
        #node.ssh.execute('mkdir -p /data/s3/foundationmedicine')

        # copy credentials
        master.ssh.execute('scp /root/.s3cfg %s:/root/.s3cfg' % (node.alias))
        master.ssh.execute('scp /root/.passwd-s3fs %s:/root/.passwd-s3fs' % (node.alias))

        # sync user permissions
        master.ssh.execute('scp /etc/group %s:/etc/group' % (node.alias))

        #node.ssh.execute('if mount | grep /data/s3/basespacebackup; then umount -l /data/s3/basespacebackup && s3fs basespacebackup /data/s3/basespacebackup -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs basespacebackup /data/s3/basespacebackup -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
        node.ssh.execute('if mount | grep /data/s3/averapatients; then umount -l /data/s3/averapatients && s3fs averapatients /data/s3/averapatients -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs averapatients /data/s3/averapatients -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
        node.ssh.execute('if mount | grep /data/s3/averaprojects; then umount -l /data/s3/averaprojects && s3fs averaprojects /data/s3/averaprojects -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs averaprojects /data/s3/averaprojects -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
        node.ssh.execute('if mount | grep /data/s3/averafastq; then umount -l /data/s3/averafastq && s3fs averafastq /data/s3/averafastq -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs averafastq /data/s3/averafastq -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
        node.ssh.execute('if mount | grep /data/s3/averamirt; then umount -l /data/s3/averamirt && s3fs averamirt /data/s3/averamirt -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs averamirt /data/s3/averamirt -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')
        #node.ssh.execute('if mount | grep /data/s3/foundationmedicine; then umount -l /data/s3/foundationmedicine && s3fs foundationmedicine /data/s3/foundationmedicine -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; else s3fs foundationmedicine /data/s3/foundationmedicine -o allow_other,uid=1002,gid=100,umask=0002,use_cache=/tmp; fi')

	# add basic system monitoring
	node.ssh.execute('apt-get install -y sysstat')
	master.ssh.execute('scp /root/chkh.sh %s:/root/chkh.sh' % (node.alias))

        #add cron job to clear out the s3fs cache that is older then 12 hours, run every minute
        node.ssh.execute("echo '* * * * * find /mnt/tmp/avera*/ -type f -mmin +$((60*12)) -exec rm -f '{}' \;' >> /var/spool/cron/crontabs/root")
	node.ssh.execute("echo '*/5 * * * * /root/chkh.sh' >> /var/spool/cron/crontabs/root")
	node.ssh.execute('sed -i "1iMAILTO=\'\'" /var/spool/cron/crontabs/root')
