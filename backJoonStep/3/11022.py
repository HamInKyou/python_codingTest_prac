"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""

import sys;
input = sys.stdin.readline;

t = int(input());
for i in range(1,t+1):
    a, b = map(int, input().split());
    print(f"Case #{i}: {a} + {b} = {a+b}")