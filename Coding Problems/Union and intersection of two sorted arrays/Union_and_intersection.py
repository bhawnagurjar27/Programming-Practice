number_of_testcases = int(input())

for _ in range(number_of_testcases):
    array_size1, array_size2 = map(int, input().split())
    
    array_elements1 = list(map(int, input().split()))
    array_elements2 = list(map(int, input().split()))
    array = []
    i = 0
    j  =0
    
    while i < len(array_elements1) and j < len(array_elements2):           #For finding Union of two arrays
            if array_elements1[i] < array_elements2[j]:
                #print(array_elements1[i])
                array.append(array_elements1[i])
                i = i + 1
                
            elif array_elements1[i] > array_elements2[j]:
                #print(array_elements2[j])
                array.append(array_elements2[j])
                j = j + 1
                
            else:
                array.append(array_elements2[j])
                j = j + 1 
                i = i + 1
            
    #print(array)
    if i == len(array_elements1):
        while j < len(array_elements2):
            array.append(array_elements2[j])
            j += 1
    
    else:
        while i < len(array_elements1):
            array.append(array_elements1[i])
            i += 1
   
    print("Union of two arrays is:" +str(array))        
    
                                                                         #Intersection of two arrays
    
    print("Intersection of two arrays is:", end = " ")
    
    for i in range(array_size1):
        for j in range(array_size2):
            if array_elements1[i] == array_elements2[j]:
                print(array_elements1[i], end = " ")
                break
    print()        
    
