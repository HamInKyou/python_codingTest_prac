array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)-1,0,-1): #0번째 인덱스부터 시작이므로, array크기보다 하나적게 (+1해도 배열 끝 넘어가지 않게)
    for j in range(i): #배열 전체 탐색을 여러번 반복 (맨 뒤에는 큰것들이 쌓임 )
        if array[j] > array[j+1]: #큰것들 뒤로 보내기
            array[j], array[j+1] = array[j+1], array[j];

print(array);