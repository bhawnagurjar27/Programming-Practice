number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    num = int(input())
    factorial = 1
    if(num <= 1):
        print(1)
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
    

        print(factorial)   
    