number_of_testcases = int(input())
for _ in range(number_of_testcases):
   N = int(input())
   array = list(map(int, input().split()))
   kth_smallest_element = int(input())
   array.sort()
   #print(array)

   print(array[kth_smallest_element-1])