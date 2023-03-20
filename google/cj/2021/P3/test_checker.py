# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import sys
import codecs

# ------------------------------------------
# FUNCTION pass_test
# ------------------------------------------
def pass_test(my_file_1, my_file_2):
    # 1. We create the output variable
    res = True

    # 2. We open both files
    my_input_stream_1 = codecs.open(my_file_1, "r", encoding="utf-8")
    my_input_stream_2 = codecs.open(my_file_2, "r", encoding="utf-8")

    # 3. We read the full content of each file, removing any empty lines and spaces
    content_1 = [ line.strip().replace(" ", "") for line in my_input_stream_1 if line ]
    content_2 = [ line.strip().replace(" ", "") for line in my_input_stream_2 if line ]

    # 4. We close the files
    my_input_stream_1.close()
    my_input_stream_2.close()

    # 5. We check that both files are equal
    size_1 = len(content_1)

    # 5.1. If both files have the same length
    if (size_1 == len(content_2)):
        # 5.1.1. We compare them line by line
        for index in range(size_1):
            if (content_1[index] != content_2[index]):
                res = False
                break

    # 5.2. If the files have different lengths then they are definitely not equal
    else:
        res = False

    # 6. We return res
    return res

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We get the input values
    my_solution = "output.txt"
    expected_solution = "expected_output.txt"

    # 1.1. If the program is called from console, we modify the parameters
    if (len(sys.argv) > 1):
        # 2.1. We get the student folder path
        my_solution = sys.argv[1]

        # 2.2. We get the templates path
        expected_solution = sys.argv[2]

    # 2. We check if my_solution matches the expected_solution
    res = pass_test(my_solution, expected_solution)

    # 3. We print whether we pass the test or not
    print(res)
