number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    total_price = int(input())
    count_min_number_of_menus = 0
    price_of_menus = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    
    for price in range(len(price_of_menus)):
        while total_price >= price_of_menus[price]:
            total_price = total_price - price_of_menus[price]
            count_min_number_of_menus += 1
    
    print(count_min_number_of_menus)    