
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
# FUNCTION primes_from_1_to_n
# ------------------------------------------
def primes_from_1_to_n(n):
    # 1. We generate the variable to output
    res = []

    # 2. We traverse our candidates
    candidate = 2

    # 3. We foundd the first n prime numbers
    while (candidate <= n):

        # 3.1. We traverse all numbers in [2..(candidate-1)] to find if there is any divisor
        index = 3
        divisor_found = False

        while ((index < (candidate / 2)) and (divisor_found == False)):
            # 3.1.1. If the number is a divisor, we stop
            if (candidate % index) == 0:
                divisor_found = True
            # 3.1.2. If it is not, we continue with the next number
            else:
                index = index + 1

        # 3.2. If the number is a prime
        if divisor_found == False:
            # 3.2.1. We include the prime number in the list
            res.append(candidate)

        # 3.3. We increase candidate, to test the next integer as prime number
        candidate = candidate + 1

    # 4. We return res
    return res

# ------------------------------------------
# FUNCTION strategy
# ------------------------------------------
def strategy(test_index, prime_numbers, products_table, prime_products, my_output_stream):
    # 1. We print the start of the result
    my_output_stream.write("Case #" + str(test_index) + ": ")

    # 2. We compute the sorted list of primes used

    # 2.1. We collect all primes being used
    primes_used = {}
    for item in prime_products:
        (a,b) = products_table[item]
        primes_used[a] = True
        primes_used[b] = True

    # 2.2. We dump them to a list
    primes_list = []
    for key in primes_used:
        primes_list.append(key)

    # 2.3. We sort this list
    primes_list.sort()

    # 3. We associate each prime to a letter
    primes_to_letters = {}

    ord_letter = ord("A")
    for item in primes_list:
        primes_to_letters[ item ] = chr(ord_letter)
        ord_letter = ord_letter + 1

    # 4. We get the letter to start with

    # 4.1. We look for the first conflict-less point
    cl_index = 0
    while (prime_products[cl_index] == prime_products[cl_index + 1]):
        cl_index = cl_index + 1

    # 4.2. We get the fist letter of this conflict-free position
    a = products_table[ prime_products[cl_index] ][0]
    b = products_table[ prime_products[cl_index] ][1]
    c = products_table[ prime_products[cl_index + 1] ][0]
    d = products_table[ prime_products[cl_index + 1] ][1]
    dummy_list = [a,b,c,d]

    current_prime = a
    if dummy_list.count(a) >= 2:
        current_prime = b

    # 4.3. We move backwards until getting the very first letter
    while (cl_index > 0):
        a = products_table[prime_products[cl_index - 1]][0]
        b = products_table[prime_products[cl_index - 1]][1]

        if (current_prime == a):
            current_prime = b
        else:
            current_prime = a

        cl_index = cl_index - 1

    # 5. We write the message

    # 5.1. We write the first letter
    my_output_stream.write(primes_to_letters[current_prime])

    # 5.2. We traverse the products to print the remaining letters
    for value in prime_products:
        # 5.2.1. We get the two primes leading to it
        p1 = products_table[value][0]
        p2 = products_table[value][1]

        # 5.2.2. We print the new letter and update our current prime
        if (p1 != current_prime):
            my_output_stream.write(primes_to_letters[p1])
            current_prime = p1
        else:
            my_output_stream.write(primes_to_letters[p2])
            current_prime = p2

    # 5.3. We print the end of line character
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

    # 2. We compute the prime numbers
    prime_numbers = primes_from_1_to_n(10000)
    size = len(prime_numbers)

    # 3. We compute their products
    products_table = {}
    for i in range(0, size):
        for j in range(i, size):
            value = prime_numbers[i] * prime_numbers[j]
            products_table[value] = (prime_numbers[i], prime_numbers[j])

    # 4. We start solving the testcases one by one
    for index in range(num_test_cases):
        # 4.1. We discard the first line
        line = my_input_stream.readline()

        # 4.2. We get the list of products
        line = my_input_stream.readline()
        line = line.replace('\n', '')
        prime_products = line.split(" ")
        prime_products = list(map(int, prime_products))

        # 4.3. We solve the problem
        strategy(index+1, prime_numbers, products_table, prime_products, my_output_stream)

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
