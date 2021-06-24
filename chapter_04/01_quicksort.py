def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


arr = [34, 456, 1, 7865, 3, -54, 567, 332, 345]

print(quicksort(arr))