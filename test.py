def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left) + middle + quicksort(right)
    
arr = [3, 5, 1, 7, 2, 8, 4]
sorted_arr = quicksort(arr)
print(sorted_arr)

