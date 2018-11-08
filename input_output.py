# Optimize:

# STEP 1 - Sort each row prior to creating tuples.
# This allows to create the tuple regardless of the Artists order in a row.
# Artists [A,B] and [B,A] will generate same tuple [A,B] with itertools.
# Combinations method if the row is sorted.

# STEP 2 - The input file is iterated once.

# STEP 3 - The output file is populated while counting tuples.
#  As soon as tuple count reaches 50, the line is written into otput csv.


import argparse
import os.path


# This is the error handler if file does not exist


def check_input_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s you requested does not exist!" % arg)
    else:
        return arg


# handling input/output


def parse_args():

    parser = argparse.ArgumentParser(
        description=("Take input from ${input_file}, "
                     "create an output file ${output_file} "
                     "with a list of pairs of artists that appear TOGETHER "
                     "in at least ${list_count} different lists. "
                     "If no matches found - return an empty list."))

    parser.add_argument('--inputfile',
                        metavar='FILE',
                        default='input.txt',
                        type=lambda x: check_input_file(parser, x),
                        help=("TXT Input File location. "
                              "- default: input.txt"))

    parser.add_argument('--outputfile',
                        metavar='FILE',
                        default='output.csv',
                        help=("CSV Output File location. "
                              "Running program will override the current file "
                              "or create a new file if it doesnt exist. "
                              "- default: output.csv"))

    parser.add_argument('--listcount',
                        metavar='N',
                        type=int,
                        default=50,
                        help=("Number of times that a tuple should appear "
                              "before being written into the output file. "
                              "In this case it is 50. "
                              "Range [1-1000]. - default: 50"))

    args = parser.parse_args()

    return args
