def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

list1 = [27, 13, 1, 15, 64, 33, 49]
sorted = selection_sort(list1)
print(sorted)
