"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

단어와 반복 횟수를 입력받아 여러 번 출력해보자.

예시
w, n = input().split()
print(w*int(n))

참고
문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.
"""

word, n = input().split();
print(word*int(n));