n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# 오름차순 정렬
a.sort()
# 내림차순 정렬
b.sort(reverse=True)

for i in range(k):
    # A의 원소가 B보다 작을 때 바꿈
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: 
        break

print(sum(a))
