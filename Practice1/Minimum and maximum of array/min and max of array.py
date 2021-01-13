N = int(input())
array = list(map(int, input().split()))
array.sort()
max_array = array[-1]
min_array = array[0]
print(max_array, min_array)