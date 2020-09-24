import math

number_of_testcases = int(input())

for i in range(number_of_testcases):
    N = int(input())
    X = math.sqrt(N)             # Compute the square root
    
    
    print(math.floor(X))
