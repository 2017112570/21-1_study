n,k = map(int,input().split())
count = 0

while True:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
    if n == 1:
        break
print(count)


''' sol.1 '''
n,k = map(int,input().split())
result = 0
# n이 k 이상이라면 k로 계속 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
print(result)


''' sol.2 '''
n,k = map(int,input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n-target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1싹 빼기
result += (n-1)
print(result)
