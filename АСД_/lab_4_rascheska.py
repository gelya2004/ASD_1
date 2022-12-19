arr = [3,14,1,7,9,8,11,6,4,2]
def sort(arr):
    lens = len(arr)
    gap = int(lens/1.247)
    swap = 1
    while gap > 1 or swap > 0:
        swap = 0
        i = 0
        while i + gap < lens:
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swap += 1
            i = i + 1
        if gap > 1:
            gap = int(gap / 1.247)
            print(arr)
print(arr)
sort(arr)
print("result",arr)
