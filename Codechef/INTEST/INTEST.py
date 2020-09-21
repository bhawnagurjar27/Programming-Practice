num_testcase, divisor = map(int, input().split())

count_of_divisible_num = 0
for i in range(num_testcase):
    dividend = int(input())
    
    if dividend % divisor == 0:
        count_of_divisible_num += 1

print(count_of_divisible_num)