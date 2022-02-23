# 이건 내 풀이
# import sys;
# input = sys.stdin.readline;

# INF = 999;
# n,m = map(int, input().split());
# graph = [];
# for _ in range(n):
#     graph.append(list(map(int,input().rstrip())));
# dx = (-1, 0, 1, 0); #위, 오른쪽, 아래, 왼쪽
# dy = (0, 1, 0, -1); #위, 오른쪽, 아래, 왼쪽

# def dfs(x, y, count):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return INF;

#     if graph[x][y] == 1:
#         graph[x][y] = 0;
#         count+=1;
#         if x == n-1 and y == m-1:
#             return count;
#         resultArr = [];
#         for i in range(4):
#             nx = x + dx[i];
#             ny = y + dy[i];
#             resultArr.append(dfs(nx,ny,count));
#         return min(resultArr);
#     return INF;

# print(dfs(0,0,0));
        
import sys;
from collections import deque;
input = sys.stdin.readline;

n, m = map(int, input().split());
graph = [];
for _ in range(n):
    graph.append(list(map(int, input().rstrip())));

dx = (-1, 0, 1, 0); #위, 오른쪽, 아래, 왼쪽
dy = (0, 1, 0, -1); #위, 오른쪽, 아래, 왼쪽

def bfs(x,y):
    queue = deque();
    queue.append((x,y));

    while queue:
        x, y = queue.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue;
            if graph[nx][ny] ==0:
                continue;
            if graph[nx][ny] == 1: #방문처리하고 큐에 삽입하기
                graph[nx][ny] = graph[x][y] + 1;
                queue.append((nx,ny));
    
    return graph[n-1][m-1];

print(bfs(0,0));
