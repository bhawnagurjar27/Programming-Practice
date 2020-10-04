number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    work_done_per_day_at_office = list(map(int, input().split()))
    sum_of_work_done_per_day = 0
    
    #work_done_per_day_at_office[5] = work_done_at_home equivalent to 1 hour
    
    for i in range(0,5):
        sum_of_work_done_per_day =sum_of_work_done_per_day + (work_done_per_day_at_office[5] * work_done_per_day_at_office[i])
    
    if sum_of_work_done_per_day > 120:
        print("Yes")
    else:
        print("No")
