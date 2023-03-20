
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
# FUNCTION row_has_repeated_values
# ------------------------------------------
def row_has_repeated_values(row_values):
    # 1. We output the result variable
    res = 0

    # 2. We create an auxiliary dictionary
    my_dict = {}

    # 3. We traverse the values
    for val in row_values:
        if val in my_dict:
            res = 1
            break
        else:
            my_dict[val] = True

    # 4. We return res
    return res

# ------------------------------------------
# FUNCTION update_rows_to_check
# ------------------------------------------
def update_rows_to_check(row_values, cols_to_check, cols_values):
    # 1. We get the list of values to delete
    keys_to_delete = []

    # 1. We check each column with no values repeated so far
    for col_index in cols_to_check:
        # 1.1. If the value is repeated in the column we are looking for
        if (row_values[col_index] in cols_values[col_index]):
            # 1.1.1. We reset the dictionary, as we will not be using it anymore
            cols_values[col_index] = {}

            # 1.1.2. We remove the entry from cols_to_check
            keys_to_delete.append(col_index)

        # 1.2. If the value was not repeated
        else:
            # 1.2.1. We insert it in the associated dictionary
            cols_values[col_index][row_values[col_index]] = True

    # 2. We delete the keys that are no longer needed:
    for index in keys_to_delete:
        del cols_to_check[index]

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_input_stream, my_output_stream, test_index):
    # 1. We create the output variable

    # 1.1. We output the trace
    res_trace = 0

    # 1.2. We output the num of rows with repeated numbers
    res_num_rows = 0

    # 1.3. We output the num of columns with repeated numbers
    res_num_cols = 0

    # 2. We read the size of the matrix --> N
    n = int(my_input_stream.readline().replace("\n", ""))

    # 3. We distinguish the case in which N == 0 or N == 1
    if (n == 0):
        pass
    elif (n == 1):
        res_trace = int(my_input_stream.readline().replace("\n", ""))

    # 4. We cover the remaining interesting cases, in which N > 1
    else:
        # 4.1. We create auxiliary variables regarding the columns to be checked
        cols_to_check = { index: True for index in range(n) }
        cols_values = [{} for _ in range(n)]

        # 4.2. We traverse the rows of the matrix
        for index in range(n):
            # 4.2.1. We get the values of the row
            row_values = list(map(int, my_input_stream.readline().replace("\n", "").split(" ")))

            # 4.2.2. We update the trace
            res_trace += row_values[index]

            # 4.2.3. We found if the row has repeated values
            res_num_rows += row_has_repeated_values(row_values)

            # 4.2.4. We update the cols_to_check
            update_rows_to_check(row_values, cols_to_check, cols_values)

        # 4.3. We get the value for res_num_cols
        res_num_cols = n - len(cols_to_check)

    # 5. We print the result by the standard output
    my_str = "Case #" + str(test_index) + ": " + str(res_trace) + " " + str(res_num_rows) + " " + str(res_num_cols) + "\n"
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
