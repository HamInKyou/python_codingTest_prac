#파라메트릭 서치란 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
#ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
#일반적으로 코딩테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있다.
#제안하는 범위가 엄청 크다면 이진탐색을 써볼 것!

import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
arr = list(map(int,input().split()));

#이진탐색 위한 시작점과 끝점 설정
start = 0
end = max(arr);

result = 0;
#이진탐색 수행
while(start <= end):
    total = 0; #잘려나간 총 떡의 길이
    mid = (start + end) // 2; #떡 자를 위치(중간) 설정
    for x in arr: #떡 자르기
        if x > mid: #절단기로 잘랐을 때 떡이 남으면
            total += x - mid; #잘려나간 떡 길이에 합산
    if total < m: #잘려나간게 원하는 만큼보다 적으면
        end = mid - 1; #더 많이 잘라서 많이 남기기(절단기 사이즈 줄여서 다시 자르기)
    else: #질려나간게 원하는 만큼보다 크거나 같으면
        result = mid; #더 큰게 있을 수 있으니 일단 현재 절단기 사이즈를 저장
        start = mid + 1; #절단기 사이즈를 늘려서 다시 잘라보기

print(result)