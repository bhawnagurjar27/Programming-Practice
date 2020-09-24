number_of_testcases = int(input())

for i in range(number_of_testcases):
    num = int(input())
    sum_of_all_digits = 0

    while(num > 0):
        remainder = num % 10
        sum_of_all_digits = sum_of_all_digits + remainder
        num = num // 10
    

    print(sum_of_all_digits)    
        