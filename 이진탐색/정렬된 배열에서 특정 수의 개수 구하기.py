from bisect import bisect_left,bisect_right

n,x = map(int,input().split())
arr = list(map(int,input().split()))

# 개수 반환
def count_num(arr,left,right):
    right_idx = bisect_right(arr,right)
    left_idx = bisect_left(arr,left)
    return right_idx-left_idx

# x개의 개수
cnt = count_num(arr,x,x)

if cnt == 0:
    print(-1)
else:
    print(cnt)