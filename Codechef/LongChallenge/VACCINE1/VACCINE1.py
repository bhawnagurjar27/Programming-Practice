Day_1, Vaccines_per_day_1, Day_2, Vaccines_per_day_2, total_vaccines = map(int, input().split())
answer = 0
required_num_of_days = 0

if Day_1 == Day_2 and Day_1 == 1:
    while answer < total_vaccines:
        required_num_of_days += 1
        answer += (Vaccines_per_day_1 + Vaccines_per_day_2)
    
    print(required_num_of_days)    
        
else:
    required_num_of_days = min(Day_1, Day_2)-1
    
    while answer < total_vaccines:
        
        if Day_1 > Day_2:
            answer += Vaccines_per_day_2
            Day_2 += 1
        
        elif Day_2 > Day_1:
            answer += Vaccines_per_day_1
            Day_1 += 1
       
        elif Day_1 == Day_2:
            answer += (Vaccines_per_day_1 + Vaccines_per_day_2)
            
        
        required_num_of_days += 1
    
    print(required_num_of_days)    
            