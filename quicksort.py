def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


list1 = [27, 13, 1, 15, 64, 33, 49]
sorted_result = quick_sort(list1)
print(sorted_result)
