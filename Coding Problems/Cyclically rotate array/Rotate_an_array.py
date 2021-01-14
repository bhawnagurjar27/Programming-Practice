number_of_testcases = int(input())

for _ in range(number_of_testcases):
    array_size = int(input())
    array_elements = list(map(int, input().split()))
    
    last_element = array_elements[-1]
    for i in range(array_size-1, 0, -1):
        array_elements[i] = array_elements[i-1]
    
    array_elements[0] = last_element
        
    print(array_elements)              #Cyclically rotated array    
    