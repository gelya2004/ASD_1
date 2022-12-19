arr = [3,2,4,11,14,-9]
lens=len(arr)
for i in range(1,lens):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            print(arr)
        else:
            break
print("result",arr)
