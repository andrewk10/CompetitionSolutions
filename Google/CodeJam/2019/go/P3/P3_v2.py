
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
import math

# ------------------------------------------
# FUNCTION my_gcd
# ------------------------------------------
def my_gcd(a, b):
    # 1. We create the ouptut variable
    res = a

    # 2. While b != 0
    while (b != 0):
        aux = b
        b = res % b
        res = aux

    # 3. We return res
    return res

# ------------------------------------------
# FUNCTION strategy
# ------------------------------------------
def strategy(test_index, prime_products, my_output_stream):
    # 1. We print the start of the result
    my_output_stream.write("Case #" + str(test_index) + ": ")

    # 2. We compute the sorted list of primes used, and the products they led to

    # 2.1. Initially we start with empty tables
    primes_used = {}
    products_table = {}

    # 2.2. We get the first conflict-free point
    cl_index = 0
    while (prime_products[cl_index] == prime_products[cl_index + 1]):
        cl_index = cl_index + 1

    # 2.3. We get the two-consecutive different products
    prod1 = prime_products[cl_index]
    prod2 = prime_products[cl_index + 1]

    # 2.4. We get their factors
    p_common = math.gcd(prod1, prod2)
    p1 = prod1 // p_common
    p2 = prod2 // p_common

    # 2.5. We mark the primes as used
    primes_used[p_common] = True
    primes_used[p1] = True
    primes_used[p2] = True

    # 2.6. We mark the products too
    products_table[prod1] = (p_common, p1)
    products_table[prod2] = (p_common, p2)

    # 2.7. We traverse the rest of the products
    size = len(prime_products)
    for index in range(cl_index+1, size-1):
        # 2.7.1. We collect each two-consecutive products
        prod1 = prime_products[index]
        prod2 = prime_products[index + 1]

        # 2.7.2. If they are different:
        if (prod1 != prod2):
            # 2.7.2.1. We get their factors
            p_common = math.gcd(prod1, prod2)
            p1 = prod1 // p_common
            p2 = prod2 // p_common

            # 2.7.2.2. We mark all primes as used
            primes_used[p_common] = True
            primes_used[p1] = True
            primes_used[p2] = True

            # 2.7.2.3. We mark the products too
            products_table[prod1] = (p_common, p1)
            products_table[prod2] = (p_common, p2)

    # 3.3. We dump them to a list
    primes_list = []
    for key in primes_used:
        primes_list.append(key)

    # 3.4. We sort this list
    primes_list.sort()

    # 4. We associate each prime to a letter
    primes_to_letters = {}

    ord_letter = ord("A")
    for item in primes_list:
        primes_to_letters[ item ] = chr(ord_letter)
        ord_letter = ord_letter + 1

    # 5. We get the letter to start with

    # 5.1. We look for the first conflict-less point
    cl_index = 0
    while (prime_products[cl_index] == prime_products[cl_index + 1]):
        cl_index = cl_index + 1

    # 5.2. We get the fist letter of this conflict-free position
    a = products_table[ prime_products[cl_index] ][0]
    b = products_table[ prime_products[cl_index] ][1]
    c = products_table[ prime_products[cl_index + 1] ][0]
    d = products_table[ prime_products[cl_index + 1] ][1]
    dummy_list = [a,b,c,d]

    current_prime = a
    if dummy_list.count(a) >= 2:
        current_prime = b

    # 5.3. We move backwards until getting the very first letter
    while (cl_index > 0):
        a = products_table[prime_products[cl_index - 1]][0]
        b = products_table[prime_products[cl_index - 1]][1]

        if (current_prime == a):
            current_prime = b
        else:
            current_prime = a

        cl_index = cl_index - 1

    # 6. We write the message

    # 6.1. We write the first letter
    my_output_stream.write(primes_to_letters[current_prime])

    # 6.2. We traverse the products to print the remaining letters
    for value in prime_products:
        # 6.2.1. We get the two primes leading to it
        p1 = products_table[value][0]
        p2 = products_table[value][1]

        # 6.2.2. We print the new letter and update our current prime
        if (p1 != current_prime):
            my_output_stream.write(primes_to_letters[p1])
            current_prime = p1
        else:
            my_output_stream.write(primes_to_letters[p2])
            current_prime = p2

    # 6.3. We print the end of line character
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
        # 2.1. We discard the first line
        line = my_input_stream.readline()

        # 2.2. We get the list of products
        line = my_input_stream.readline()
        line = line.replace('\n', '')
        prime_products = line.split(" ")
        prime_products = list(map(int, prime_products))

        # 2.3. We solve the problem
        strategy(index+1, prime_products, my_output_stream)

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
