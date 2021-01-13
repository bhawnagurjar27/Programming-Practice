num_test_cases = int(input())
while num_test_cases > 0:
    N =int(input())
    red = input()
    red_count = 0
    blue_count = 0
    red = list(map(int,red))
    blue = input()
    blue = list(map(int,blue))
    for i in range(N):
        if red[i] > blue[i]:
            red_count = red_count + 1 
        elif red[i] < blue[i]:
            blue_count = blue_count + 1 
    if red_count == blue_count:
        print("EQUAL")
    elif red_count> blue_count:
        print("RED")
    else:
        print("BLUE")
            
    num_test_cases = num_test_cases - 1