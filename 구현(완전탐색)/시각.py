n=int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # i,j,k 중 3이 있는 경우의 수
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
