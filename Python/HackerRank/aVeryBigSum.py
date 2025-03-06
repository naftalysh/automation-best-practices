"""
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description
====================
Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):
    int ar[n]: an array of integers .

Return
    long: the sum of all array elements

Input Format

The first line of the input consists of an integer
.
The next line contains

space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.

Constraints

1 <= n <= 10
0 <= ar[i] <= 10**10

Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005

Output
5000000015

Note:
The range of the 32-bit integer is (-2**31 - to 2**31 - 1)
When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums. 

Answer:
When working in Python, you don't need to worry about integer overflow when summing large numbers, 
as Python's int type is designed to handle arbitrarily large values gracefully. This feature simplifies numerical computations, 
allowing you to focus on your algorithms without concern for integer overflow issues. 

# Summing a list of large integers in Python
large_numbers = [2**30, 2**30, 2**30, 2**30]   #[1073741824, 1073741824, 1073741824, 1073741824]
total_sum = sum(large_numbers)
print(total_sum)  # Output: 4294967296

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here

    # Ensure input is a list with exactly ar[0]+1 elements
    assert isinstance(ar, list) and 1 <= len(ar) <= 10, "Input 'ar' is a list and must have between 1 to 10 elements"

     # Add assertions for value range
    assert all(0 <= x <= 10**10 for x in ar), "All elements must satisfy 0 <= x <= 10**10"

    # sum = 0
    # for i in range(1, ar[0]):
    #     sum += ar[i]

    total_sum = sum(ar)
    # assert 0 <= total_sum <= 2**31 - 1, "total_sum must satisfy 0 <= x <= 2**31 - 1"

    return total_sum




if __name__ == '__main__':
     # Set OUTPUT_PATH to the current working directory if not already set
    os.environ['OUTPUT_PATH'] = os.path.join(os.getcwd(), 'output.txt')

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())
    assert 1 <= ar_count <= 10, "0 <= ar_count must <= 10"

    ar = list(map(int, input().strip().split()))
    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()

    # debug
    print(result)

