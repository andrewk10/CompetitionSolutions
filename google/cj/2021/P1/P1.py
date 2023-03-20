
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
# FUNCTION find_j
# ------------------------------------------
def find_j(l, i):
    # 1. We output the position of the smallest item from the index i onwards
    res = i

    # 2. We store the value
    lb = l[i]

    # 3. We traverse the remaining items
    index = i + 1
    for item in l[i+1:]:
        # 3.1. If the new item is smallest than lb
        if (item < lb):
            # 3.1.1. We reset the dictionary, as we will not be using it anymore
            lb = item
            res = index

        # 3.2. We increase the index
        index += 1

    # 4. We return res
    return res

# ------------------------------------------
# FUNCTION compute_cost
# ------------------------------------------
def compute_cost(l, n):
    # 1. We create the output variable
    res = 0

    # 2. We do the iterations
    for i in range(n - 1):
        # 2.1. We find j
        j = find_j(l, i)

        # 2.2. We revert l
        aux = l[i:j + 1][:]
        aux.reverse()
        l = l[0:i] + aux + l[j + 1:n]

        # 2.3. We update res
        res += (j - i) + 1

    # 3. We return res
    return res

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_input_stream, my_output_stream, test_index):
    # 1. We create the output variable
    res = 0

    # 1.1. We output the num_items
    n = 0

    # 1.2. We output the list of items
    l = []

    # 2. We read the size of the list --> N
    n = int(my_input_stream.readline().replace("\n", ""))

    # 3. We distinguish the case in which N < 2
    if (n < 2):
        pass

    # 4. We read and process the list
    else:
        # 4.1. We read the list
        l = list(map(int, my_input_stream.readline().strip().split(" ")))

        # 4.2. We compute the cost
        res = compute_cost(l, n)

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
