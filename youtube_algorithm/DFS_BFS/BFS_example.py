from collections import deque;

def bfs(graph, start, visited):
    queue = deque([start]) #시작노드 집어넣고 시작
    visited[start] = True;

    while queue:
        v = queue.popleft() #큐에서 원소 뽑기
        print(v, end=" ");
        for i in graph[v]:
            if not visited[i]:
                queue.append(i);
                visited[i] = True

graph = [ #2차원 리스트로 각 노드가 연결된 정보를 표현 
    [], #0번 (패스 -> 1번부터 표현)
    [2, 3, 8], #1번 노드와 연결된 노드들
    [1, 7], #2번 노드와 연결된 노드들
    [1, 4, 5], #3
    [3, 5], #4
    [3, 4], #5
    [7], #6
    [2, 6, 8], #7
    [1, 7] #8
]

visited = [False] * 9 #각 노드 방문 체크하는 리스트

bfs(graph, 1, visited)