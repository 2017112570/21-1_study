n = int(input())
count = 0

# 동전 단위
coin_list = [500,100,50,10]

for coin in coin_list: # coin_list에서 큰 단위부터
    count += n//coin
    n %= coin

print(count)