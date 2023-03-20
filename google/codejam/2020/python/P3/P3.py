
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
# FUNCTION find_schedule
# ------------------------------------------
def find_schedule(n, activity_times, ordered_indexes):
    # 1. We create the output variable
    res = ()

    # 1.1. We output whether there is a valid schedule
    is_valid = True

    # 1.2. We output such schedule
    schedule = [0] * n

    # 2. We set the next availability time of Cameron and Jamie
    available_times = [0, 0]

    # 3. We traverse the activities, in case they are available
    for index in range(n):
        # 3.1. We get the position and the activity
        pos = ordered_indexes[index]
        activity = activity_times[pos]

        # 3.2. If the activity can be assigned to Cameron, we do
        if (activity[0] >= available_times[0]):
            available_times[0] = activity[1]
        # 3.3. Otherwise
        else:
            # 3.3.1. If the activity can be assigned to Cameron, we do
            if (activity[0] >= available_times[1]):
                schedule[pos] = 1
                available_times[1] = activity[1]
            # 3.3.2. Otherwise there is no feasible schedule
            else:
                is_valid = False
                break

    # 4. We assign res
    res = (is_valid, schedule)

    # 5. We return res
    return res

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_input_stream, my_output_stream, test_index):
    # 1. We create the output variable
    my_str = "IMPOSSIBLE"

    # 2. We read the number of activities --> N
    n = int(my_input_stream.readline().replace("\n", ""))

    # 3. We read the time of the activities
    activity_times = [ (0, 0) ] * n
    for index in range(n):
        activity_times[index] = tuple(map(int, my_input_stream.readline().replace("\n", "").split(" ")))

    # 4. We get an array with the indexes for the sorted activities by increasing starting time
    ordered_indexes = sorted(range(len(activity_times)), key=lambda k: activity_times[k])

    # 5. We find a valid timetable
    (is_valid, schedule) = find_schedule(n, activity_times, ordered_indexes)

    # 6. If the schedule is valid, we edit it
    if (is_valid == True):
        my_str = "".join(map(str, schedule))
        my_str = my_str.replace("0", "C").replace("1", "J")

    # 7. We print the result by the standard output
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
