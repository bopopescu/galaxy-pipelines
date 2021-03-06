#!/usr/bin/env python

# The Galaxy server calls this Python script and this Python script will use 
# the parameters from the Galaxy server to a) generate a parameter file,
# b) generate a workflow_file, and c) constitute the command to run the the
# workflow. For example,
# 
# this script will generate a parameter file that looks like this:
#
# TODO: Finish this part
#
# and will run a command that looks like this:
#
# python runWorkflow.py -w wf_hanb.txt -i default.txt -o /some/output/dir/in/the/cluster -d biocore -u tester
# Author: Yu Fu (yfu@yfu.me)

import optparse
# Consider use argparse instead. argparse is only available in Python 2.7
# or newer.
from optparse import OptionParser
from subprocess import call

import re
import os
import sys
import random

index_location = "/share/zzpipeline/pipeline/bowtie/indexes"

def main():
    # print sys.argv
    
    usage = """usage: python %prog [options] arg

The Galaxy server calls this Python script and this Python script will use the parameters from the Galaxy server to a) generate a parameter file for the workflow and b) constitute the command to run the the workflow.

Please email yfu@yfu.me for bugs or questions."""
    parser = OptionParser(usage=usage, version="%prog 0.1")
    parser.add_option("-i", "--input", action="store", type="string",
                      dest="input",
                      help="Inserts file")

    # -o is no longer useful as the result will be under 
    parser.add_option("-o", "--output-dir", action="store", type="string",
                      dest="output",
                      help="Output directory")

    parser.add_option("-a", "--adaptor", action="store", type="string",
                      dest="adaptor", help="Adaptor sequence")
    
    parser.add_option("-s", "--min", action="store", type="string",
                      dest="min", help="Minimum length of inserts")
    
    parser.add_option("-l", "--max", action="store", type="string",
                      dest="max", help="Maximum length of inserts")
    
    parser.add_option("-m", "--mm", "--mismatch", action="store",
                      type="string", dest="mm", help="Mismatches allowed")
    
    parser.add_option("-f", "--female", dest="female", action="store",
                      help="FEMALE sample")
    
    parser.add_option("-e", "--email", action="store",
                      type="string", dest="email", help="Email address to be notified")
    
    parser.add_option("--location", action="store",
                      dest="location",
                      help="The location specified by the galaxy service. This script will create the corresponding parameter file and workflow file under that directory")
    parser.add_option("-u", "--user-email", action="store", dest="user_email",
                      help="Get the user's email address from the galaxy service")
    

    # The following options are on longer useful
    # parser.add_option("-w", "--workflow-file", action="store", type="string",
    #                   dest="workflow_file",
    #                   help="Specify where to store the workflow file. This should be passed from the Galaxy server to this script")
    
    # parser.add_option("-p", "--parameter-file", action="store",
    #                   dest="parameter_file", help="The location for the parameter file of the workflow (specified by Galaxy server)")
    
    (options, args) = parser.parse_args()

    print "Options from Galaxy server:"
    print options
    print

    input_file = options.input
    # output_dir = options.output
    adaptor = options.adaptor
    minimum = options.min
    maximum = options.max
    mm = options.mm
    female = options.female
    email = options.email
    location = options.location

    user_email = options.user_email
    # print input_file, output_dir, species, cpu, config, default_param_file
    pat = re.compile(r"(.*)@")
    m = pat.match(user_email)
    username = ""
    try:
        username = m.group(1)
    except:
        sys.stderr.write("Wrong username!")
        exit(1)
        
    basename = os.path.basename(location)
    dirname = os.path.dirname(location)

    f_o = open(location, "w")
    parameter_file = os.path.join(dirname, basename + ".param")
    workflow_file = os.path.join(dirname, basename + ".workflow")
    
    f_p = open(parameter_file, "w")
    f_w = open(workflow_file, "w")
    # Maybe use the default parameter file on the server side
    # For now, I will just write all the parameters on the client side
    print >> f_p, "@BASH=/bin/bash"
    print >> f_p, "@PERL=/share/bin/perl"
    print >> f_p, "@PYTHON=/share/bin/python"

    # print >> f_p, "@INPUT_FILE=" + input_file
    # Note that later in the script, I created a symlink for the original file
    input_file_basename = os.path.basename(input_file)
    # This is not a platform-neutral solution.
    # I do not expect this to run in Windows, though.

    unified = "/isilon_temp/weng/fuy2/public/output"
    id = str(random.randrange(1, 1000000000))
    loc = unified + "/" + username + "_" + id

    msg = "You can find your result via the following url:\n" + \
    "http://biocore.umassmed.edu/genome/smallRNA/" + username + "_" + id \
    + "\n\n" + "Otherwise, you can find the results on the cluster here:\n" \
    + loc

    print >> f_o, msg
    
    print >> f_p, "@INPUT_FILE=" + loc + "/" + input_file_basename
    print >> f_p, "@OUTPUT_DIR=" + loc
    print >> f_p, "@ADAPTOR=" + adaptor
    print >> f_p, "@MINIMUM=" + minimum
    print >> f_p, "@MAXIMUM=" + maximum
    print >> f_p, "@MM=" + mm
    print >> f_p, "@EMAIL=" + email
    if female == 't':
        print >> f_p, "@FEMALE=" + 'Y'
    else:
        print >> f_p, "@FEMALE=" + 'N'
    # This indicates the real bash script to run. runWorkflow.py just submits
    # the one-line workflow.
    # I may probably move the pipeline to my isilon_temp space. For now
    # I just use the one under Zhiping's directory
    # print >> f_p, "@PIPELINEDIR=/isilon_temp/weng/fuy2/public/Hanb/small_RNA_pipeline"
    print >> f_p, "@PIPELINEDIR=/home/wengz/pipelines/smallRNApipeline/pipeline_dm"

    workflow_command = ["@BASH", "@PIPELINEDIR/zpipe_TAS_new.sh",
                        "@INPUT_FILE", "@ADAPTOR", "@MINIMUM", "@MAXIMUM", "@MM", "@FEMALE", "@EMAIL", "I_am_a_boring_job_id", index_location]
    ld_library_path = """/home/hanb/software/Development/seqan-trunk/extras/include:/home/hanb/lib64:/home/hanb/include:/home/hanb/lib:/share/bin/gcc/lib64:/share/bin/gcc/lib:/share/bin/mpfr/lib:/share/bin/gmp/lib:/home/wangw1/src/libgtextutils-0.6/lib:/lib:/usr/lib:/usr/local/lib:/opt/SUNWhpc/HPC8.1/gnu/lib/lib64:/share/bin/gcc/lib64:/share/bin/gcc/lib:/share/bin/intel/fc/10.1.015/lib:/share/bin/intel/fc/10.1.015/licenses:/share/bin/intel/cc/10.1.015/lib:/share/bin/mpfr/lib:/share/bin/gmp/lib:/share/lib:""" # This is Wei's LD_LIBRARY_PATH
    path = """/home/wangw1/src/jdk1.6.0_37/bin:/home/wangw1/bin/python2.7:/home/wangw1/src/bwa-0.7.5a:/home/wangw1/perl5/bin:/share/bin/gcc/bin:/share/bin:/opt/SUNWhpc/HPC8.1/gnu/bin/:/share/bin/intel/bin/intel64:/share/bin/gmp/include:/share/bin/mpfr/include:/sge/bin/lx24-amd64:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin::/home/wangw1/bin::/home/wangw1/localperl/bin::/home/wangw1/src/pcre-8.31::/home/wangw1/src/R-2.15.3::/home/wangw1/src/ucsc_tools:/home/wangw1/bin/samtools::/home/wangw1/src/libgtextutils-0.6/:/home/wangw1/src/libgtextutils-0.6/include/gtextutils/gtextutils::/home/wangw1/src/libgtextutils-0.6/bin::/home/wengz/pipelines/smallRNApipeline/pipeline_dm/:/home/wengz/pipelines/smallRNApipeline/transposon_bucket/::/home/wengz/pipelines/smallRNApipeline/bin::/home/wangw1/src/bowtie-0.12.9:/home/wangw1/src/bowtie2-2.1.0::/home/wangw1/src/circos-0.56:/home/wangw1/src/circos-0.56/bin::/home/wangw1/src/trinityrnaseq_r2013-02-25::/home/wangw1/src/trinityrnaseq_r2013-02-25/trinity-plugins/jellyfish-1.1.6/bin:/home/wangw1/src/trinityrnaseq_r2013-02-25/trinity-plugins/parafly:/home/wangw1/src/bedtools-2.17.0/bin/bedtools:/home/wangw1/src/bedtools-2.17.0/bin::/home/wangw1/src/msort::/home/wangw1/src/HTSeq-0.5.4p2::/home/wangw1/src/trinityrnaseq_r2013-02-25/trinity-plugins/rsem:/home/wangw1/src/STAR_2.3.0e::/home/wangw1/src/tophat-2.0.9.Linux_x86_64::/home/wangw1/src/cufflinks-2.1.1.Linux_x86_64::/home/wangw1/src/numpy-1.6.1::/home/wangw1/src/weblogo-3.2::/home/hanb/bin:/home/hanb/include:/home/hanb/lib::/home/wangj2/bin::/share/bin/gcc/bin:/share/bin:/opt/SUNWhpc/HPC8.1/gnu/bin/:/share/bin/intel/bin/intel64:/share/bin/gmp/include:/share/bin/mpfr/include:/sge/bin/lx24-amd64:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin::/home/wangw1/src/sratoolkit.2.1.10-centos_linux64/bin:""" # This is Wei's PATH

    # print default_param_file
    # The pipeline itself should have the capability to output the results to
    # any dir......

    print >> f_w, "CreateOutputDir" + "\t" + "mkdir -p " + loc + "/output" + "\t" + "1"
    print >> f_w, "Symlink" + "\t" + "ln -fs " + input_file + " " + loc + "/" + input_file_basename + "\t" + "1"
    print >> f_w, "Final" + "\t" + "export PATH=$PATH:" + path +  "&& export LD_LIBRARY_PATH=" + ld_library_path +  "&&" + " " . join(workflow_command) + "\t" + "1"
    f_o.close()
    f_p.close()
    f_w.close()
    
    # TODO: Change this when migrated to the server
    # client = "/isilon_temp/garber/bin/runWorkflow.py"
    client = "/isilon_temp/weng/fuy2/public/runWorkflow.py"
    
    # The following makes sure that a runWorkflow.py file is available
    try:
        open(client)
    except IOError:
        client = "/home/fuy2/galaxy_pipeline/runWorkflow.py"
        
    print "The client (runWorkflow.py) that I use:"
    print client
    print

    # The workflow file is generated on the fly
    
    command = ["python", client, "-w", workflow_file, "-d", "galaxyweb", "-i", parameter_file]
    print "I will run the following command to call runWorkflow.py"
    print command

    # Prepare for the environment variables.
    # The following should have been integrated into Wei's pipeline.
    my_env = os.environ.copy()

    print my_env

    my_env["PATH"] = path
    try:

        my_env["LD_LIBRARY_PATH"] = ld_library_path + my_env["LD_LIBRARY_PATH"]
    except:
        my_env["LD_LIBRARY_PATH"] = ld_library_path
    
    call(command, env=my_env)
    print "Done!"
    
if __name__ == "__main__":
    main()
