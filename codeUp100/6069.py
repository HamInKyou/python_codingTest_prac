"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
"""

c = input();
result = ""
if c == 'A':
    result = "best!!!";
elif c == 'B':
    result = "good!!"
elif c == 'C':
    result = "run!"
elif c == 'D':
    result = "slowly~"
else:
    result = "what?"
print(result)