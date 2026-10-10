def bubble_sort(list):
    n=len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j+1],list[j]=list[j],list[j+1]
    return list
list1=[27,13,1,15,64,33,49]
sorted=bubble_sort(list1)
print(sorted)
