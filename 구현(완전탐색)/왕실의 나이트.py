data = input()
row = int(data[1])
#아스키 코드 'a' = 97
column = int(ord(data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

count = 0
for step in steps:
    # 이동하고자 하는 위치
    next_row = row + step[0]
    next_column = column +step[1]

    if (1 <= next_row <= 8) and (1 <= next_column <= 8):
        count += 1

print(count)