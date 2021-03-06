from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class SNPiRInstaller(ClusterSetup):
	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			log.info("Installing SNPiR 1.0 scripts on %s" % (node.alias))
			node.ssh.execute('mkdir -p /opt/software/snpir/1.0/bin')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/bin http://lilab.stanford.edu/SNPiR/BLAT_candidates.pl')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/SNPiR http://lilab.stanford.edu/SNPiR/config.pm')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/bin http://lilab.stanford.edu/SNPiR/convertCoordinates.class')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/bin http://lilab.stanford.edu/SNPiR/convertCoordinates.java')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/bin http://lilab.stanford.edu/SNPiR/convertVCF.sh')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/bin http://lilab.stanford.edu/SNPiR/filter_homopolymer_nucleotides.pl')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/bin http://lilab.stanford.edu/SNPiR/filter_intron_near_splicejuncts.pl')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/bin http://lilab.stanford.edu/SNPiR/filter_mismatch_first6bp.pl')
			node.ssh.execute('wget -c -P /opt/software/snpir/1.0/bin http://lilab.stanford.edu/SNPiR/readme')
			node.ssh.execute('chmod +x /opt/software/snpir/1.0/bin/filter*')
			node.ssh.execute('chmod +x /opt/software/snpir/1.0/bin/convertVCF.sh')
			node.ssh.execute('chmod +x /opt/software/snpir/1.0/bin/BLAT_candidates.pl')

			log.info("Configuring SNPiR")
			node.ssh.execute("sed -i /opt/software/snpir/1.0/SNPiR/config.pm -e '17s/.*/our \$BLATEXE = \x27\/opt\/software\/ucsc\/287\/blat\x27;/'")
			node.ssh.execute("sed -i /opt/software/snpir/1.0/SNPiR/config.pm -e '18s/.*/our \$SAMTOOLSEXE = \x27\/opt\/software\/samtools\/samtools-1.1\/samtools\x27;/'")
			node.ssh.execute("sed -i /opt/software/snpir/1.0/SNPiR/config.pm -e '19s/.*/our \$FASTAFROMBED = \x27\/opt\/software\/bedtools\/bedtools2.21\/bin\/fastaFromBed\x27;/'")
			
			log.info("Creating SNPiR Module")
			node.ssh.execute('mkdir -p /usr/local/Modules/applications/snpir/;touch /usr/local/Modules/applications/snpir/1.0')
			node.ssh.execute('echo "#%Module" >> /usr/local/Modules/applications/snpir/1.0')
			node.ssh.execute('echo "set root /opt/software/snpir/1.0" >> /usr/local/Modules/applications/snpir/1.0')
			node.ssh.execute('echo -e "prepend-path\tPATH\t\$root/bin" >> /usr/local/Modules/applications/snpir/1.0')
