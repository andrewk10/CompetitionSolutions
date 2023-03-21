
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
# 1. FUNCTION parse_in
# ------------------------------------------
def parse_in(my_input_stream):
    # 1. We create the output variable
    res = []

    # 2. We get the number of test cases
    line = my_input_stream.readline()
    line = line.replace("\n", "")
    num_test_cases = int(line)

    # 3. We get the list of test cases
    for index in range(num_test_cases):
        # 3.1. We get the line
        line = my_input_stream.readline()

        # 3.2. We replace the end of line
        line = line.replace('\n', '')
        num = int(line)

        # 3.3. We append it to rides
        res.append(num)

    # 4. We return res
    return res

# ------------------------------------------
# 2. FUNCTION parse_out
# ------------------------------------------
def parse_out(my_output_stream, output_info):
    # 1. We traverse output_info so as to print it
    index = 1
    for item in output_info:
        # 2.1. We create the line to write
        my_str = "Case #" + str(index) + ": " + str(item[0]) + " " + str(item[1]) + "\n"

        # 2.2. We print the line
        my_output_stream.write(my_str)

        # 2.3. We increase index
        index = index + 1

# ------------------------------------------
# 3. FUNCTION strategy
# ------------------------------------------
def strategy(input_info):
    # 1. We create the output variable
    res = []

    # 2. We solve the different test cases
    for n in input_info:
        # 2.1. We set up a and b
        found = False
        a = 1
        b = n-1

        # 2.2. We traverse the posibilities until we find a valid one
        while ((found == False) and (a <= b)):
            if (("4" not in str(a)) and ("4" not in str(b))):
                found = True
            else:
                a = a + 1
                b = b - 1

        # 2.3. We append the solution to the list
        res.append( (a,b) )

    # 3. We return res
    return res

# ------------------------------------------
# 3. FUNCTION remove_4
# ------------------------------------------
def remove_4(n, mode):
    # 1. We create the output variable
    res = 0

    # 2. We get the string version of n and its length
    str_n = str(n)
    len_n = len(str_n)

    # 3. We traverse these digits, so as to find the 4 and thus the value to subtract
    digit = 0
    found = False
    while ((found == False) and (digit < (len_n - 1))):
        # 3.1. If the digit is not a 4, we continue looking for it
        if (str_n[digit] != "4"):
            digit = digit + 1
        # 3.2. If it is
        else:
            # 3.2.1. If we are removing the 4 from b, we subtract the reminder
            if (mode == False):
                res = int(str_n[(digit + 1):]) + 1
            # 3.2.2. If we are removing the 4 from a, we add what its left to get rid of the reminder
            else:
                res = (10 ** (len_n - (digit + 1))) - int(str_n[(digit + 1):])
            # 3.2.3. We end our search
            found = True

    # 4. If 4 was not found it is because it was the last digit
    if (found == False):
        res = 1

    # 5. We return res
    return res


# ------------------------------------------
# 3. FUNCTION strategy2
# ------------------------------------------
def strategy2(input_info):
    # 1. We create the output variable
    res = []

    # 2. We solve the different test cases
    for n in input_info:
        # 2.1. We set up a and b
        found = False
        a = 1
        b = n-1

        # 2.2. We set the turn to b
        a_turn = False

        # 2.2. We traverse the posibilities until we find a valid one
        while ((found == False) and (a <= b)):
            # 2.1. If both a and b are 4-free, we are done
            if (("4" not in str(a)) and ("4" not in str(b))):
                found = True
            # 2.2. If not, we have to update the one containing a 4
            else:
                # 2.3. We compute the value so as to get rid of the 4
                if (a_turn == True):
                    value = remove_4(a, a_turn)
                else:
                    value = remove_4(b, a_turn)

                # 2.4. We update a and b accordingly with this value
                a = a + value
                b = b - value

                # 2.5. We swap the turn
                a_turn = not a_turn

        # 2.3. We append the solution to the list
        res.append( (a,b) )

    # 3. We return res
    return res

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_input_stream, my_output_stream):
    # 1. We do the parseIn from the input file
    input_info = parse_in(my_input_stream)

    # 2. We do the strategy to solve the problem
    output_info = strategy2(input_info)

    # 3. We do the parse out to the output file
    parse_out(my_output_stream, output_info)

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
