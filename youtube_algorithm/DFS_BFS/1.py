import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
graph = [];
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False;
    if graph[x][y] == 0: #지금 현재 위치와 인접한 모든 부분을 방문하여 1로 메꿔준다(재귀적으로)
        graph[x][y] = 1; #일단 현재 위치 체크
        dfs(x-1, y) #상
        dfs(x, y-1) #좌
        dfs(x +1, y) #하
        dfs(x, y+1) #우
        return True;
    return False; #지금 위치가 이미 방문한 위치라면 세지 않는다!

result = 0;
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1;

print(result)