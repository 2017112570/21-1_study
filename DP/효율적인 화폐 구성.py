# n = 화폐의 단위, m = 화폐의 합
n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

dp = [10001]*(m+1)

# 상향식(바텀업) DP
dp[0] = 0

for i in range(n): # 화폐 단위
    for j in range(arr[i],m+1): # 화폐 금액
        if dp[j-arr[i]] != 10001:
            dp[j] = min(dp[j],dp[j-arr[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])