"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!!!!!!"""

while True:
3	    try:
4	        print("Enter a list of numbers separated by commas: ")
5	        numbers = [float(value) for value in input().split(",")]
6	    except ValueError:
7	        print("Some input could not be converted to a number!")
8	    else:
9	        sizeOfNumbers = len(numbers)
10	        if (sizeOfNumbers % 2 == 0):
11	            median = (numbers[(sizeOfNumbers // 2) ] + numbers[(sizeOfNumbers // 2) - 1]) / 2
12	            print(median)
13	        else:
14	            median = numbers[sizeOfNumbers//2]
15	            print(median)
16	        print(numbers)
