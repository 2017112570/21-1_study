n = int(input())
array = []
for i in range(n):
    a,b = input().split()
    b = int(b)
    array.append((a,b))

array.sort(key=lambda x:x[1])
for i in range(n):
    print(array[i][0],end = ' ')
