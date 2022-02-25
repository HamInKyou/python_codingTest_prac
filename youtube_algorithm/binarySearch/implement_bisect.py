#파이썬 이진탐색 라이브러리
from bisect import bisect_left, bisect_right;

arr = [1,2,4,4,8];
x = 4;
print(bisect_left(arr,x)); #정렬된 순서를 유지하면서 배열 arr에 x를 삽입할 가장 왼쪽 인덱스 반환 
print(bisect_right(arr,x)); #정렬된 순서를 유지하면서 배열 arr에 x를 삽입할 가장 오른쪽 인덱스 반환
