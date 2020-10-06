number_of_testcases = int(input())

for _ in range(number_of_testcases):
	# Read integers a and b.
	num1, num2 = map(int, input().split(' '))
	
	sum1 = num1 + num2
	print(sum1)