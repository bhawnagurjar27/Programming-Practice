number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    N = int(input())
    array = list(map(int, input().split()))
    
    count_of_subarrays = 0
    
    for i in range(N):
        sum_of_elements_of_subarray = 0
        product_of_elements_of_subarray = 1
        
        for j in range(i, N):
            sum_of_elements_of_subarray = sum_of_elements_of_subarray + array[j]
            product_of_elements_of_subarray = product_of_elements_of_subarray * array[j]
            
            if sum_of_elements_of_subarray == product_of_elements_of_subarray:        # If sum is equal to product then increment count
                                                                                        
                                                                                      
               count_of_subarrays = count_of_subarrays + 1
            
   
    print(count_of_subarrays)
    
        