def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) 
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


list1 = [27, 13, 1, 15, 64, 33, 49]
sorted_result = merge_sort(list1)
print(sorted_result)
