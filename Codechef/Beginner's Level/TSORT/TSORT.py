number_of _numbers_in_list = int(input())

list_of_numbers = []
for i in range(number_of_numbers_in_list):
    N = int(input())
    list_of_numbers.append(N)
    
list_of_numbers.sort()

for i in list_of_numbers:             # Print sorted list
    print(i) 

        