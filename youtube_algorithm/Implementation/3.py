import sys;
input = sys.stdin.readline;

positionStr = input().rstrip();
x = ord(positionStr[0])-ord('a')+1;
y = int(positionStr[1]);

dx = [-2,-1,1,2,2,1,-1,-2];
dy = [1,2,2,1,-1,-2,-2,-1];

cnt = 0;
for i in range(8):
    nx = x + dx[i];
    ny = y + dy[i];

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue;
    cnt+=1;

print(cnt);


