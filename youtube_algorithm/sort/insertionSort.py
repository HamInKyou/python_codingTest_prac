array = [ 7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

for i in range(1, len(array)): #0번째 인덱스는 이미 정렬완료되었다 치고 1번 인덱스부터
    for j in range(i, 0, -1): #현재 삽입해야할 인덱스부터 맨 처음까지 어디에 넣을지 탐색
        if array[j] < array[j-1]: #정렬이 될 수 있도록 앞에거랑 바꿔가면서 반복 이어나가기
            array[j], array[j -1] = array[j-1], array[j];
        else:  #더이상 바꿀게 없으면 삽입 완료되었다 치고 다음 인덱스로
            break;

print(array)