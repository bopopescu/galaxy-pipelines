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

# TODO: Remove this
import sys
import re
import os
import random

def main():
    # print sys.argv
    
    usage = """usage: python %prog [options] arg

The Galaxy server calls this Python script and this Python script will use the parameters from the Galaxy server to a) generate a parameter file for the workflow and b) constitute the command to run the the workflow.

Please email yfu@yfu.me for bugs or questions."""
    parser = OptionParser(usage=usage, version="%prog 0.1")
    parser.add_option("-i", "--input", action="store", type="string",
                      dest="input",
                      help="Input file in fastq or gzipped fastq format, with full directory")

    # -o option is no longer useful as all outputs go to a random dir under
    # /isilon_temp/weng/fuy2/public/output/
    # parser.add_option("-o", "--output-dir", action="store", type="string",
    #                   dest="output",
    #                   help="Output directory")
    
    parser.add_option("-s", "--species", action="store", type="string",
                      dest="species",
                      help="Species [ human | mouse | mm10 | fly ]")
    # No need to handle the default of cpu. run.sh will handle it
    # parser.add_option("-c", "--cpu", action="store", type="int", dest="cpu",
    #                   default=8,
    #                   help="Number of CPUs to use, default: %default")
    parser.add_option("-c", "--cpu", action="store", type="int", dest="cpu",
    #                  default=8,
                      help="Number of CPUs to use, default: %default")

    parser.add_option("-f", "--config", action="store", dest="config")
    # For example, the location can be /some/dir/galaxy-dist/database/files/
    # dateset_123.dat. This script will create dataset_123.dat.workflow and
    # dataset_123.dat.param under the same dir. The name is a bit
    # counterintuitive....
    parser.add_option("-l", "--location", action="store",
                      dest="location",
                      help="The location specified by the galaxy service. This script will create the corresponding parameter file and workflow file under that directory")
    parser.add_option("-w", "--workflow-file", action="store", type="string",
                      dest="workflow_file",
                      help="Specify where to store the workflow file. This should be passed from the Galaxy server to this script")
    parser.add_option("-u", "--user-email", action="store", dest="user_email",
                      help="Get the user's email address from the galaxy service")
    (options, args) = parser.parse_args()

    print "Options from Galaxy server:"
    print options
    print

    input_file = options.input
    # output_dir = options.output
    species = options.species
    cpu = options.cpu
    config = options.config
    location = options.location
    user_email = options.user_email

    # Parse the email to get the username. I need to pass the username to
    # runWorkflow.py
    pat = re.compile(r"(.*)@")
    m = pat.match(user_email)
    username = ""
    try:
        username = m.group(1)
    except:
        sys.stderr.write("Wrong username!")
        exit(1)
    # print input_file, output_dir, species, cpu, config, default_param_file

    basename = os.path.basename(location)
    dirname = os.path.dirname(location)

    # This is where the script write userful info for end users
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

    print >> f_p, "@INPUT_FILE=" + input_file

    # Uncomment the following line if you want the user able to write the
    # result anywhere.
    # print >> f_p, "@OUTPUT_DIR=" + output_dir

    # example: fuy2_13456736 folder
    unified = "/isilon_temp/weng/fuy2/public/output"
    id = str(random.randrange(1, 1000000000))
    loc = unified + "/" + username + "_" + id

    msg = "You can find your result via the following url:\n" + \
      "http://biocore.umassmed.edu/genome/smallRNA/" + username + "_" + id \
      + "\n\n" + "Otherwise, you can find the results on the cluster here:\n" \
      + loc

    print >> f_o, msg


    print >> f_p, "@OUTPUT_DIR=" + loc
    # This indicates the real bash script to run. runWorkflow.py just submits
    # the one-line workflow. 
    print >> f_p, "@PIPELINEDIR=/isilon_temp/weng/fuy2/public/Hanb/small_RNA_pipeline"

    workflow_command = ["@BASH", "@PIPELINEDIR/run.sh", "-i", "@INPUT_FILE",
                        "-o", "@OUTPUT_DIR", "-s", species]

    # print default_param_file
    if cpu is not None:
        print >> f_p, "@NUMBER_CPU=" + str(cpu)
        workflow_command.append("-c")
        workflow_command.append("@NUMBER_CPU")
    if config is not None:
        print >> f_p, "@CONFIG_FILE=" + config
        workflow_command.append("-f")
        workflow_command.append("@CONFIG_FILE")

    print >> f_w, "StepOne" + "\t" + " " . join(workflow_command) + "\t" + "1"
    
    f_o.close()
    f_p.close()
    f_w.close()
    
    # TODO: Change this when migrated to the server
    # client = "/isilon_temp/garber/bin/runWorkflow.py"
    client = "/isilon_temp/weng/fuy2/public/runWorkflow.py"
    
    # The following makes sure that a runWorkflow.py file is available
    try:
        # This client should be used when it is migrated to galaxy server
        open(client)
    except IOError:
        # This client should work when I debug it on zlab3 and zlab4
        client = "/home/fuy2/galaxy_pipeline/runWorkflow.py"
        
    print "The client (runWorkflow.py) that I use:"
    print client
    print

    # The workflow file is generated on the fly
    
    command = ["python", client, "-w", workflow_file, "-d", "biocoreweb", "-i", parameter_file, "-u", username]
    print "I will run the following command to call runWorkflow.py"
    print command

    call(command)
    print "Done!"
    
if __name__ == "__main__":
    main()
