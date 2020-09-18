
num_testcase, dividend = map(int, input().split())
count_divisible_num = 0
for i in range(num_testcase):
    divisor = int(input())
    if divisor % dividend == 0:
        count_divisible_num += 1

print(count_divisible_num)