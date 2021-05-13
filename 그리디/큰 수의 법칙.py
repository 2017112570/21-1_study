''' sol.1 '''
# 배열의 크기 n, 숫자가 더해지는 횟수 m, 최대 횟수 k
n,m,k = map(int,input().split())
n_list = list(map(int,input().split()))
result =0

n_list.sort()
first = n_list[n-1]
second = n_list[n-2]

while True:
    for i in range(k): # 가장 큰 수를 k번 더함
        if m == 0: # m = 0일 때, while문 탈출
            break
        result += first
    if m == 0: # m = 0일 때, while문 탈출
        break
    result += second
    m -= 1

print(result)


''' sol.2 '''
n,m,k = map(int,input().split())
n_list=list(map(int,input().split()))
result = 0

n_list.sort()
first = n_list[n-1]
second = n_list[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1)

result += count * first
result += (m-count) * second
print(result)
