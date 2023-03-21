
# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs

# ------------------------------------------
# FUNCTION strategy
# ------------------------------------------
def strategy(test_index, maze_size, lydia_movs, my_output_stream):
    # 1. We print the start of the result
    my_output_stream.write("Case #" + str(test_index) + ": ")

    # 2. We create some auxiliary variables
    rows = 0

    # 2. We traverse the movements
    for index in range(maze_size-1):
        # 2.1. We get the two movements of Lydia
        fs = lydia_movs[(2 * index):((2 * index) + 2)]

        # 2.2. Depending on Lydia's movement

        # 2.2.1. ES
        if (fs == "ES"):
            my_output_stream.write("SE")

        # 2.2.2. SE
        elif (fs == "SE"):
            my_output_stream.write("ES")

        # 2.2.3. EE and rows 0
        elif ((fs == "EE") and (rows == 0)):
            my_output_stream.write("SE")
            rows = rows + 1

        # 2.2.4. EE and rows -1 (and, by extension, any other value)
        elif ((fs == "EE") and (rows != 0)):
            my_output_stream.write("ES")
            rows = rows + 1

        # 2.2.5. SS and rows 0
        elif ((fs == "SS") and (rows == 0)):
            my_output_stream.write("ES")
            rows = rows - 1

        # 2.2.6. SS and rows 1 (and, by extension, any other value)
        elif ((fs == "SS") and (rows != 0)):
            my_output_stream.write("SE")
            rows = rows - 1

    my_output_stream.write("\n")

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_input_stream, my_output_stream):
    # We merge the steps 1 (parse_in), 2 (strategy) and 3 (parse_out) for memory reasons

    # 1. We get the number of test cases
    line = my_input_stream.readline()
    line = line.replace("\n", "")
    num_test_cases = int(line)

    # 2. We start solving the testcases one by one
    for index in range(num_test_cases):
        # 3.1. We get the size of the maze
        line = my_input_stream.readline()
        line = line.replace('\n', '')
        maze_size = int(line)

        # 3.2. We get the movements from Lydia
        line = my_input_stream.readline()
        lydia_movs = line.replace('\n', '')

        # 3.3. We solve the problem
        strategy(index+1, maze_size, lydia_movs, my_output_stream)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Submission Flag
    submit = True

    # 2. We set up the parameter names
    input_file_name = "input.txt"
    output_file_name = "output.txt"

    # 3. We set up our input and output streams
    my_input_stream = None
    my_output_stream = None

    if submit == True:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout
    else:
        my_input_stream = codecs.open(input_file_name, "r", encoding="utf-8")
        my_output_stream = codecs.open(output_file_name, "w", encoding="utf-8")

    # 4. We solve the problem
    my_main(my_input_stream, my_output_stream)

    # 5. If needed, we close the files
    if submit == False:
        my_input_stream.close()
        my_output_stream.close()
