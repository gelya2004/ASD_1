array = [2, 44, 5, 11, 22, 4]
print("Исходный массив", array)
def heapify(array, lens, i):
    largest = i
    left = 2 * i + 1 
    right = 2 * i + 2
    if left < lens and array[i] < array[left]:
        largest = left
    if right < lens and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, lens, largest)
def heapSort(array):
    lens = len(array)
    for i in range(lens // 2, -1, -1):
        heapify(array, lens, i)
    for i in range(lens-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
        print("Очередная итерация", array)
    return array
noviyspisok = heapSort(array).copy()
print('Результат сортировки:', noviyspisok)
