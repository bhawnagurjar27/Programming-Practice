number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    count_of_first_guard, count_of_seconed_guard = map(int, input().split())
    
    print(max(count_of_first_guard, count_of_seconed_guard), count_of_seconed_guard + count_of_first_guard)