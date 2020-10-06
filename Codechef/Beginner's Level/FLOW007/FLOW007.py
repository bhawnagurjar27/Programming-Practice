number_of_testcases = int(input())

for _ in range(number_of_testcases):
    N = int(input())
    reverse_of_number = 0
    
    while(N != 0):
        remainder = N % 10                   # Find the reaminder
        reverse_of_number = reverse_of_number * 10 + remainder
        N = N // 10                          # Find the quotient
    
    
    print(reverse_of_number)    
    