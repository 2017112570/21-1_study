n,m = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
end = max(arr)

# 최대 높이
h = 0

# 이진 탐색
while start <= end:
    cnt = 0
    # 중간점 지정 = 높이
    mid = (start+end)//2

    for i in arr:
        if i >= mid:
            cnt += i-mid
    
    # 왼쪽 탐색
    if cnt < m:
        end = mid -1

    # 오른쪽 탐색
    else:
        h = mid
        start = mid +1

print(h)
