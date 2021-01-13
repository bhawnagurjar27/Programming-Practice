import math

number_of_testcases = int(input())

for _ in range(number_of_testcases):
    number_of_people, vaccinate_people_per_day = map(int,input().split())
    age_of_people = list(map(int,input().split()))
    people_at_risk = 0
    people_not_at_risk = 0
    number_of_days_to_vaccinate_everyone = 0
    
    for i in range(number_of_people):
        if age_of_people[i] >= 80 or age_of_people[i] <= 9:
            people_at_risk += 1 
        
        else:
            people_not_at_risk += 1
    
    number_of_days_to_vaccinate_everyone = math.ceil(people_at_risk / vaccinate_people_per_day) + math.ceil(people_not_at_risk / vaccinate_people_per_day)        
    
    print(number_of_days_to_vaccinate_everyone)       