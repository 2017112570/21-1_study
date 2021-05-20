n,m = map(int,input().split())
d=[[0]*m for _ in range(n)]
x,y,direction = map(int,input().split())
d[x][y] = 1 #현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int,input().split())))
# 북서남동
dx = [-1,0,1,0]
dy = [0,-1,0,1]

count = 1
turn = 0
while True:
    # 왼쪽으로 회전
    direction -= 1
    if direction < 0:
        direction = 3
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn = 0
        continue
    # 회전 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn += 1
    # 내 방향 모두 갈 수 없는 경우
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn = 0
print(count)
