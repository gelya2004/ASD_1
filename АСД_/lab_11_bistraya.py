arr = [7, 6, 10,55,3,1,11,45,4]
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    elem = arr[0] #пусть опорным будет первый элемент
    left = list(filter(lambda x: x<elem, arr))#меньше опорного
    center = [i for i in arr if i==elem]#генератор списка потому что опорный элемент может появиться несколько раз
    right = list(filter(lambda x: x>elem, arr))#больше опорного
    return quick_sort(left)+center+quick_sort(right)
print("Исходный массив", arr)
print("Отсортированный массив", quick_sort(arr))
