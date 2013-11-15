#!/usr/bin/env python

# This script is similar to small_rna_pipeline_hanb.py
#
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

def main():
    # print sys.argv
    
    usage = """usage: python %prog [options] arg

The Galaxy server calls this Python script and this Python script will use the parameters from the Galaxy server to a) generate a parameter file for the workflow and b) constitute the command to run the the workflow.

Please email yfu@yfu.me for bugs or questions."""
    parser = OptionParser(usage=usage, version="%prog 0.1")
    parser.add_option("-a", "--input-a", action="store", type="string",
                      dest="input_a",
                      help="Input dir a in fastq or gzipped fastq format, with full directory")
    parser.add_option("-b", "--input-b", action="store", type="string",
                      dest="input_b",
                      help="Input file in fastq or gzipped fastq format, with full directory")

    parser.add_option("-o", "--output-dir", action="store", type="string",
                      dest="output",
                      help="Output directory")
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
    parser.add_option("-p", "--parameter-file", action="store",
                      dest="parameter_file",
                      help="The location for the parameter file of the workflow (specified by Galaxy server)")
    parser.add_option("-w", "--workflow-file", action="store", type="string",
                      dest="workflow_file",
                      help="Specify where to store the workflow file. This should be passed from the Galaxy server to this script")
    (options, args) = parser.parse_args()

    print "Options from Galaxy server:"
    print options
    print

    input_dir_a = options.input_a
    input_dir_b = options.input_b
    output_dir = options.output
    species = options.species
    cpu = options.cpu
    config = options.config
    parameter_file = options.parameter_file
    workflow_file = options.workflow_file
    # print input_file, output_dir, species, cpu, config, default_param_file

    f_p = open(parameter_file, "w")
    f_w = open(workflow_file, "w")
    # Maybe use the default parameter file on the server side
    # For now, I will just write all the parameters on the client side
    print >> f_p, "@BASH=/bin/bash"
    print >> f_p, "@PERL=/share/bin/perl"
    print >> f_p, "@PYTHON=/share/bin/python"

    print >> f_p, "@INPUT_DIR_A=" + input_dir_a
    print >> f_p, "@INPUT_DIR_B=" + input_dir_b
    print >> f_p, "@OUTPUT_DIR=" + output_dir
    
    # This indicates the real bash script to run. runWorkflow.py just submits
    # the one-line workflow. 
    print >> f_p, "@PIPELINEDIR=/isilon_temp/weng/fuy2/public/Hanb/small_RNA_pipeline"

    # Different from small_rna_pipeline_hanb.py (run2.sh)
    workflow_command = ["@BASH", "@PIPELINEDIR/run2.sh", "-a", "@INPUT_DIR_A",
                        "-b", "@INPUT_DIR_B", "-o", "@OUTPUT_DIR",
                        "-s", species]

    # print default_param_file
    if cpu is not None:
        print >> f_p, "@NUMBER_CPU=" + str(cpu)
        workflow_command.append("-c")
        workflow_command.append("@NUMBER_CPU")
    # if config is not None:
    #     print >> f_p, "@CONFIG_FILE=" + config
    #     workflow_command.append("-f")
    #     workflow_command.append("@CONFIG_FILE")

    print >> f_w, "StepOne" + "\t" + " " . join(workflow_command) + "\t" + "1"
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
    
    command = ["python", client, "-w", workflow_file, "-d", "biocoreweb", "-i", parameter_file]
    print "I will run the following command to call runWorkflow.py"
    print command

    call(command)
    print "Done!"
    
if __name__ == "__main__":
    main()
