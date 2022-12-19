arr = [2, 555, 77, 59, 3, 61, 10]
lens = len(arr)
rang = 10
for i in range(lens):
    lst = [[] for j in range(rang)]
    for x in arr:
        figure = x//10**i%10
        lst[figure].append(x)
    arr = []
    for k in range(rang):
        arr= arr+lst[k]
print (arr)
