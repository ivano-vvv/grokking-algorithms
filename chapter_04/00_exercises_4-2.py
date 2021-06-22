def length_of(list):
    try:
        first_item = list[0]

        list_clone = list.copy()
        list_clone.remove(first_item)

        return 1 + length_of(list_clone)
    except IndexError:
        return 0


list_1 = []
list_2 = [1]
list_3 = [23, 74, 82]

print(length_of(list_1))
print(length_of(list_2))
print(length_of(list_3))

# ========================================
# ========================================
# ========================================

# original

def count(list):
    if list == []:
        return 0
    return 1 + sum(list[1:])