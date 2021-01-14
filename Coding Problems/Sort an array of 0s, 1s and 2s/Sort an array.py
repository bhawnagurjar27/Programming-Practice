number_of_testcases = int(input())

for _ in range(number_of_testcases):
    array_size = int(input())
    array = list(map(int, input().split()))
    
    low_index = 0
    mid_index = 0
    high_index = array_size - 1 
    
    while mid_index <= high_index:
        
        if array[mid_index] == 0:
            temp = array[mid_index]
            array[mid_index] = array[low_index]
            array[low_index] = temp
            low_index += 1 
            mid_index += 1 
        
        elif array[mid_index] == 1:
            mid_index += 1 
        
        else:
            temp = array[mid_index]
            array[mid_index] = array[high_index]
            array[high_index] = temp
            high_index -= 1 
            
    print(array)      
    
    

            
     
