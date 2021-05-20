n = int(input())
routes=input().split()
x,y = 1,1
for i in routes:
    if i == 'r':
        if y < n:
            y += 1
        else:
            pass
    elif i == 'l':
        if y > 1:
            y -= 1
        else:
            pass
    elif i == 'u':
        if x > 1:
            x -= 1
        else:
            pass
    else:
        if x < n:
            x += 1
        else:
            pass
print(x,y)

''' sol '''
n=int(input())
x,y = 1,1
plans = input().split()
# l,R,U,D에 따른 이동 방향
dx=[0,0,-1,1]
dy=[-1,1,0,0]
moves_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x,y = nx,ny
print(x,y)
