number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    
    A, B = map(int, input().split())
    
    total_valid_pairs = 0
    if A % 2 == 0 and B % 2 == 0:
        total_valid_pairs += (A//2) * (B//2)
        total_valid_pairs += (A//2) * (B//2)
    
    elif A%2 != 0 and B%2 != 0:
        total_valid_pairs += ((A+1)//2) * ((B+1)//2)
        total_valid_pairs += (A//2) * (B//2)
    
    elif A%2 == 0 and B%2 != 0:
        total_valid_pairs += (A//2) * (B//2)
        total_valid_pairs += (A//2) * ((B+1)//2)
    
    elif A%2 != 0 and B%2 == 0:
        total_valid_pairs += (A//2) * (B//2)
        total_valid_pairs += ((A+1)//2) * (B//2)  
   
    
        
    print(total_valid_pairs) 