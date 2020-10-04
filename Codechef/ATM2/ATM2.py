number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    number_of_people, total_money_available = map(int, input().split())
    people_wants_to_withdraw_money = list(map(int, input().split()))
    
    answer = ''      # Here answer variable is used as string to determine whether they will get the required amount of money or not.
    
    for i in range(number_of_people):
        if people_wants_to_withdraw_money[i] <= total_money_available:
            total_money_available = total_money_available - people_wants_to_withdraw_money[i]
            answer = answer + '1'
        else:
            answer = answer + '0'
    
    print(answer)
    
            