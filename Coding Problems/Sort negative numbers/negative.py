number_of_testcases = int(input())

for _ in range(number_of_testcases):
   N = int(input())
   array = list(map(int, input().split()))
   j = 0
   for i in range(0, N):
       if array[i] < 0:
           temp = array[i]
           array[i] = array[j]
           array[j] = temp
           
           j += 1 
               
       

   print(array)