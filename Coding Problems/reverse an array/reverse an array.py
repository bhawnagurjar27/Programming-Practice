number_of_testcases = int(input())

for _ in range(number_of_testcases):
    N = int(input())
    array = list(map(int, input().split()))
    
    for i in range(N//2):
       array[i], array[N-i-1] = array[N-i-1], array[i]
    
    
    
    print(array)   
       
   
   
   
   