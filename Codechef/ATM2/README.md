# Question
https://www.codechef.com/problems/ATM2

# Approach
Initially, initialize the "answer" variable as string to determine whether they will get the required amount of money or not.

Step 1: Under the range of number of people, check whether the money which people wants to withdraw is less then or equal to the total available money in the ATM.
     
          If the above statement is TRUE, then decrease the total available money in to ATM by the money which people wants to withdraw at ith index.
        
          And append '1' into answer as string

          If above statement is FALSE, then append '0' into the answer as string on the particular ith index.

Step 2: Print answer as output