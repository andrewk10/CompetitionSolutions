
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
# FUNCTION find_list_with_cost_c
# ------------------------------------------
def find_list_with_cost_c(l, new_l, n, c, solution_found):
    # 1. We create the output variable
    res = solution_found

    # 2. Base Case: We have taken all values
    if (l == []):
        # 2.1. We get the candidate cost
        candidate_cost = compute_cost(new_l[:], n)

        # 2.2. We assign res
        res = (candidate_cost == c)

    # 3. Recursive Case: We take a new value
    else:
        for index in range(len(l)):
            # 3.1. We take the item
            item = l[index]
            del l[index]
            new_l.append(item)

            # 3.2. We solve recursively
            res = find_list_with_cost_c(l, new_l, n, c, res)

            # 3.3. We backtrack if necessary
            l.insert(index, item)
            if (res == False):
                del new_l[-1]
            else:
                break

    # 4. We return res
    return res

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_input_stream, my_output_stream, test_index):
    # 1. We create the output variable
    res = 0

    # 2. We get the values
    (n, c) = list(map(int, my_input_stream.readline().strip().split(" ")))

    # 3. We try all possibilities by brute force
    res = "IMPOSSIBLE"
    if ((c >= (n-1)) and (c < ((n * (n+1)) // 2))):
        # 3.1. We get the list of values
        l = [index for index in range(1, n+1)]

        # 3.2. We get the list
        sol_list = []
        is_solution = find_list_with_cost_c(l, sol_list, n, c, False)

        # 3.3. We get the String
        if (is_solution == True):
            res = " ".join([str(item) for item in sol_list])

    # 4. We print the solution
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

