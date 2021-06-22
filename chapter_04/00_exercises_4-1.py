def sum(arr):
    arr_length = len(arr)

    if arr_length == 0:
        return 0
    
    # unnecessary
    if arr_length == 1:
        return arr[0]

    return arr[0] + sum(arr[1:arr_length])


arr = [1, 2, 3, 4]
arr_other = [10, 20, 100, 5]

print(sum(arr))
print(sum(arr_other))

# ========================================
# ========================================
# ========================================

# original

def sum_original(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])