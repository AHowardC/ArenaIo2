import collections
import itertools
import csv
import input_output


# this is the logic for creating matches


def create_matches(input_file_location,
                   output_file_location,
                   tuple_size,
                   list_count):

    print ("Checking all favorite artists with the arguments listed below:")
    print ("Input File: {}. "
           "Output File: {}. "
           "Tuple Size: {}. "
           "List Count: {}."
           .format(
               input_file_location,
               output_file_location,
               tuple_size,
               list_count))

    favoritesDict = collections.defaultdict(int)
    matches = 0

    # Open file to write results into it.
    # This will create an empty file if there are no matches.
    with open(output_file_location, 'w') as output_file:
        csv_out = csv.writer(output_file)
        # Opening the file in order to analyze inputs.
        with open(input_file_location, 'r') as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                # if row is not empty, order it, generate possible combs.
                # take into account the size of a tuple.
                if row:
                    combinations = list(
                        itertools.combinations(sorted(row), tuple_size))
                    # iterate over the above combinations.
                    # increment occurence by one if the pair is found.
                    for combination in combinations:
                        favoritesDict[combination] += 1
                        # if a combination count reaches 50,
                        # write it to the destination file.
                        if favoritesDict[combination] == list_count:
                            csv_out.writerow(combination)
                            matches += 1

    print ("All done. "
           "Number of matches found: {}. "
           "Please check the output file: {} for matches. "
           .format(
               matches,
               output_file_location))


def main():
    # refer to args from the imported input_output file
    args = input_output.parse_args()
    create_matches(args.inputfile,
                   args.outputfile,
                   2,
                   args.listcount)


if __name__ == "__main__":
    main()
