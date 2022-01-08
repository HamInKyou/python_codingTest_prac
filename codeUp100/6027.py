"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

예시
a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

참고
10진수 형태로 입력받고
%x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
(%o로 출력하면 8진수(octal) 문자열로 출력된다.)

10진법은 한 자리에 10개(0 1 2 3 4 5 6 7 8 9)의 문자를 사용하고,
16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 a b c d e f)의 문자를 사용한다.
16진수 a는 10진수의 10, b는 11, c는 12 ... 와 같다.
"""

num = int(input());
print('%x'% num)