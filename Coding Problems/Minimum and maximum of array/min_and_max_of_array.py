number_of_testcases = int(input())

for _ in range(number_of_testcases):
    N = int(input())
    array = list(map(int, input().split()))
    max_element = array[0]
    min_element = array[0]
    
    for i in range(len(array)):
        if array[i] < min_element:
            min_element = array[i]
        
        if array[i] > max_element:
            max_element = array[i]
            
        
        
    print(max_element, min_element)   
