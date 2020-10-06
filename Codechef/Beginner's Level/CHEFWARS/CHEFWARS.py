import math
number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
	darth_health, attack_power = map(int, input().split())
	
	answer =  darth_health - attack_power
	updated_attack_power = attack_power

	while(updated_attack_power > 0 and answer > 0):
	    updated_attack_power = math.floor(updated_attack_power / 2)
	    answer = answer - updated_attack_power
	
	if(answer <= 0 and updated_attack_power > 0):
	    print('1')
	
	elif(answer > 1 and updated_attack_power == 1):
	    print('0')
	
	else:
	    print('0')