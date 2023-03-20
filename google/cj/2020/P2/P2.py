
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
# FUNCTION my_main
# ------------------------------------------
def my_main(my_input_stream, my_output_stream, test_index):
    # 1. We create the output variable
    my_str = ""

    # 2. We read the size of the matrix --> N
    digits = my_input_stream.readline().replace("\n", "")

    # 3. We get the length of the String
    size = len(digits)

    # 3. We distinguish the case in which the String is empty
    if (size == 0):
        pass

    # 4. When the String contains some digits
    else:
        # 4.1. We generate the String to get to the first digit
        my_str = my_str + ("(" * int(digits[0])) + digits[0]

        # 4.2. We traverse the transitions to the remaining digits
        for index in range(size-1):
            # 4.2.1. We get the subtraction between digit[i] and digit[i+1]
            k = int(digits[index + 1]) - int(digits[index])

            # 4.2.2. We add '(' or ')' accordingly
            if (k >= 0):
                my_str = my_str + ("(" * k) + digits[index + 1]
            else:
                my_str = my_str + (")" * ((-1) * k)) + digits[index + 1]

        # 4.3 We generate the String to get after the last digit
        my_str = my_str + (")" * int(digits[size-1]))

    # 5. We print the result by the standard output
    my_str = "Case #" + str(test_index) + ": " + my_str + "\n"
    my_output_stream.write(my_str)

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

    # 4. We read the number of test cases
    num_test_cases = int(my_input_stream.readline().replace("\n", ""))

    # 5. We solve each test case separately
    for index in range(num_test_cases):
        my_main(my_input_stream, my_output_stream, index + 1)

    # 6. If needed, we close the files
    if submit == False:
        my_input_stream.close()
        my_output_stream.close()


