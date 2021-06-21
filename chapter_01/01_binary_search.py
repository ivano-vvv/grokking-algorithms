def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

my_list = [1, 3, 5, 7, 8, 9, 13, 15, 17, 18, 24, 27, 28]

print(binary_search(my_list, 28))

