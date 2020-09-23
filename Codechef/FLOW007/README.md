# Question:
https://www.codechef.com/submit/FLOW007

# Approach
Firstly, Set reverse_of_number of to be 0.
Step 1: Check whether the given number is not equal to 0 using while loop.
Step 2: If yes, find the remainder by performing modulus of 10 with the input.
Step 3: Then, Multiply reverse_of_number by 10 and add the remainder to it, store the answer in reverse_of_number.
Step 4: Then, get the quotient of the input.
        The loop will repeat until the number is reversed.