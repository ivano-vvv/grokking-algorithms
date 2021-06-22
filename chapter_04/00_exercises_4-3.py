def max_value(list):
    length = len(list)

    if length == 0:
        return None
    
    if length == 1:
        return list[0]

    max_of_the_rest = max_value(list[1:length])

    return list[0] if list[0] >= max_of_the_rest else max_of_the_rest


list_1 = [52, 64, 2, 865, 3, 42]
list_2 = [1, 2, 3, 4]
list_3 = []
list_4 = [-1]

print(max_value(list_1))
print(max_value(list_2))
print(max_value(list_3))
print(max_value(list_4))

# ========================================
# ========================================
# ========================================

# original

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max