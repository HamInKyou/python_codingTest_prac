def dfs(graph, v, visited): #전체 그래프, 현재 노드, 방문 체크 리스트
    visited[v] = True; #현재 노드 방문체크하기
    print(v, end=' ');
    for i in graph[v]: #현재 노드와 인접한 노드들 탐색
        if not visited[i]: #방문하지 않았다면
            dfs(graph, i, visited) #거기서 부터 또 깊이우선탐색

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

dfs(graph, 1, visited);