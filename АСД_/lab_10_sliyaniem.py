arr = [1, 3, 444, 55, 66, 45]
def merge_two_list(list1,list2):
    lists = []
    i=j=0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            lists.append(list1[i])
            i+=1
        else:
            lists.append(list2[j])
            j+=1
    if i<len(list1):
        lists+=list1[i:]
    if j<len(list2):
        lists+=list2[j:]
    return lists

def merge_sort(arr):
    if len(arr)==1:
        return arr
    middle = len(arr)//2
    left = merge_sort(arr[:middle]) #срез списка с начала до середины не включительно
    right = merge_sort(arr[middle:]) #срез списка с середины и до конца
#рекурсия списков
    return merge_two_list(left, right)


print('Исходный массив:', arr)
print('Результат сортировки:', merge_sort(arr))
