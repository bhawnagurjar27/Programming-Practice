number_of_testcases = int(input())

for i in range(number_of_testcases):
    N = int(input())                    
    
    count_of_digit_four = 0
    while(N > 0):
        if(N % 10 == 4):
            count_of_digit_four = count_of_digit_four + 1              # Check if the digit is 4 
        
        N = N // 10
   
   
    print(count_of_digit_four)    