arr = [-9,5,14,0,-2,7,4]
lens = len(arr)
for i in range(lens-1):
    minn = arr[i]
    index = i
    for j in range(i+1,lens):
        if minn>arr[j]:
            minn =arr[j]
            index = j
        print(arr)
    if index!=i:
        variable = arr[i]
        arr[i]=arr[index]
        arr[index]=variable
    print(arr)
    
print("result", arr)

