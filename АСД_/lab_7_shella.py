def sortshell(arr):
    lens = len(arr)
    gap = lens//2
    while gap >0:
        for i in range(gap, lens):
            element = arr[i]
            index = i
            while index>=gap and arr[index-gap]>element:
                arr[index]=arr[index-gap]
                index-=gap
                arr[index]=element
        gap//=2
        print(arr)
    return arr
arr = [3,-4,14,0,-6,7,5]
sortshell(arr)
print("result", arr)
            
