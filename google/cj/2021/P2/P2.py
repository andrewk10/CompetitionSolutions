
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
# FUNCTION get_relevant_sub_string
# ------------------------------------------
def get_relevant_sub_string(s):
    # 1. We create the sub-String we must look at
    res = []

    # 2. We get the lower bound index
    lb = -1

    index = 0
    for char in s:
        if (char != "?"):
            break
        index += 1
    if (lb < len(s)):
        lb = index

    # 3. We get the upper bound index
    if (lb != -1):
        # 3.1. We compute the upper bound
        ub = len(s)

        index = 0
        for char in s[::-1]:
            if (char != "?"):
                break
            index += 1
        if (((ub - 1) - index) >= 0):
            ub = (ub - 1) - index

        # 3.2. If there are different
        if (lb != ub):
            # 3.2.1. We assign res to it
            res = s[lb:(ub+1)]

            # 3.2.2. We get rid of any '?' character
            res = "".join([char for char in res if (char != '?')])

    # 4. We return res
    return res

# ------------------------------------------
# FUNCTION get_cost_from_s
# ------------------------------------------
def get_cost_from_s(x, y, s):
    # 1. We output the position of the smallest item from the index i onwards
    res = 0

    # 2. We get just the relevant part of s
    s = get_relevant_sub_string(s)

    # 3. We maintain the last relevant character
    last_char = "?"

    # 4. We traverse the letters from 's' to get the non-avoidable cost
    for char in s:
        if (char == 'C') and (last_char == 'J'):
            res += x
            last_char = 'C'
        elif (char == 'J') and (last_char == 'C'):
            res += y
            last_char = 'J'

    # 5. We return res
    return res

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_input_stream, my_output_stream, test_index):
    # 1. We create the output variable
    res = 0

    # 2. We get the inputs
    x = 0
    y = 0
    s = ""

    (x, y, s) = my_input_stream.readline().strip().split(" ")
    x = int(x)
    y = int(y)

    # 3. We get just the relevant part of s
    s = get_relevant_sub_string(s)

    # 4. If the String contains any character
    if (s != []):
        # 4.1. We maintain the last relevant character
        last_char = s[0]

        # 4.2. We traverse the letters from 's' to get its cost
        for new_char in s[1:]:
            if (last_char == 'C') and (new_char == 'J'):
                res += x
                last_char = 'J'
            elif (last_char == 'J') and (new_char == 'C'):
                res += y
                last_char = 'C'

    # 5. We print the result by the standard output
    my_str = "Case #" + str(test_index) + ": " + str(res) + "\n"
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
