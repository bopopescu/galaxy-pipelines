CreateOutputDir	mkdir -p /isilon_temp/weng/fuy2/public/output/fuy2_857984278/output	1
Symlink	ln -fs /isilon_temp/weng/fuy2/public/Phil.SRA.PiwiIPago3hets.unox.ovary.inserts.trimmed /isilon_temp/weng/fuy2/public/output/fuy2_857984278/Phil.SRA.PiwiIPago3hets.unox.ovary.inserts.trimmed	1
Final	export PATH=$PATH:/home/wangw1/src/jdk1.6.0_37/bin:/home/wangw1/bin/python2.7:/home/wangw1/src/bwa-0.7.5a:/home/wangw1/perl5/bin:/share/bin/gcc/bin:/share/bin:/opt/SUNWhpc/HPC8.1/gnu/bin/:/share/bin/intel/bin/intel64:/share/bin/gmp/include:/share/bin/mpfr/include:/sge/bin/lx24-amd64:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin::/home/wangw1/bin::/home/wangw1/localperl/bin::/home/wangw1/src/pcre-8.31::/home/wangw1/src/R-2.15.3::/home/wangw1/src/ucsc_tools:/home/wangw1/bin/samtools::/home/wangw1/src/libgtextutils-0.6/:/home/wangw1/src/libgtextutils-0.6/include/gtextutils/gtextutils::/home/wangw1/src/libgtextutils-0.6/bin::/home/wengz/pipelines/smallRNApipeline/pipeline_dm/:/home/wengz/pipelines/smallRNApipeline/transposon_bucket/::/home/wengz/pipelines/smallRNApipeline/bin::/home/wangw1/src/bowtie-0.12.9:/home/wangw1/src/bowtie2-2.1.0::/home/wangw1/src/circos-0.56:/home/wangw1/src/circos-0.56/bin::/home/wangw1/src/trinityrnaseq_r2013-02-25::/home/wangw1/src/trinityrnaseq_r2013-02-25/trinity-plugins/jellyfish-1.1.6/bin:/home/wangw1/src/trinityrnaseq_r2013-02-25/trinity-plugins/parafly:/home/wangw1/src/bedtools-2.17.0/bin/bedtools:/home/wangw1/src/bedtools-2.17.0/bin::/home/wangw1/src/msort::/home/wangw1/src/HTSeq-0.5.4p2::/home/wangw1/src/trinityrnaseq_r2013-02-25/trinity-plugins/rsem:/home/wangw1/src/STAR_2.3.0e::/home/wangw1/src/tophat-2.0.9.Linux_x86_64::/home/wangw1/src/cufflinks-2.1.1.Linux_x86_64::/home/wangw1/src/numpy-1.6.1::/home/wangw1/src/weblogo-3.2::/home/hanb/bin:/home/hanb/include:/home/hanb/lib::/home/wangj2/bin::/share/bin/gcc/bin:/share/bin:/opt/SUNWhpc/HPC8.1/gnu/bin/:/share/bin/intel/bin/intel64:/share/bin/gmp/include:/share/bin/mpfr/include:/sge/bin/lx24-amd64:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin::/home/wangw1/src/sratoolkit.2.1.10-centos_linux64/bin:&& export LD_LIBRARY_PATH=/home/hanb/software/Development/seqan-trunk/extras/include:/home/hanb/lib64:/home/hanb/include:/home/hanb/lib:/share/bin/gcc/lib64:/share/bin/gcc/lib:/share/bin/mpfr/lib:/share/bin/gmp/lib:/home/wangw1/src/libgtextutils-0.6/lib:/lib:/usr/lib:/usr/local/lib:/opt/SUNWhpc/HPC8.1/gnu/lib/lib64:/share/bin/gcc/lib64:/share/bin/gcc/lib:/share/bin/intel/fc/10.1.015/lib:/share/bin/intel/fc/10.1.015/licenses:/share/bin/intel/cc/10.1.015/lib:/share/bin/mpfr/lib:/share/bin/gmp/lib:/share/lib:&&@BASH @PIPELINEDIR/zpipe_TAS_new.sh @INPUT_FILE @ADAPTOR @MINIMUM @MAXIMUM @MM @FEMALE @EMAIL I_am_a_boring_job_id /share/zzpipeline/pipeline/bowtie/indexes	1
