def find_in(int, list, iteration = 0):
    if len(list) == 0:
        print('iteration', iteration)
        return None

    mid_index = len(list) // 2
    mid_value = list[mid_index]

    if int == mid_value:
        print('iteration', iteration)
        return mid_index

    if int > mid_value:
        return find_in(int, list[mid_index:], iteration + 1)

    if int < mid_value:
        return find_in(int, list[:mid_index], iteration + 1)


print(find_in(34, range(1, 100)))
print(find_in(75, range(1, 10000)))
print(find_in(0, range(1, 100)))