import sys;
input = sys.stdin.readline;

n = int(input());
plans = list(input().split());


curX = 1;
curY = 1;

#이건 내 풀이
# for direction in plans:
#     if direction=="L":
#         if curY-1 >= 1:
#             curY-=1; 
#     elif direction=="R":
#         if curY+1 <= n:
#             curY+=1;
#     elif direction=="U":
#         if curX-1 >= 1:
#             curX-=1;
#     elif direction=="D":
#         if curX+1 <= n:
#             curX+=1;

# print(curX, curY)

dx = [0, 0, -1, 1];
dy = [-1, 1, 0, 0];
move_types = ['L','R','U','D'];

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = curX + dx[i];
            ny = curY + dy[i];
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue;
    curX, curY = nx, ny;

print(curX,curY)