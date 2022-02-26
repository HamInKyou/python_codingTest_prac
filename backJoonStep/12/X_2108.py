import sys;
from collections import Counter
input = sys.stdin.readline;

n = int(input());
numbers = []
for _ in range(n):
    num = int(input());
    numbers.append(num);

numbers.sort();

#1.산술평균
print(int(round(sum(numbers)/n)));
#2.중앙값
print(numbers[n//2]);

#3.최빈값
cntArr = Counter(numbers).most_common();
if len(cntArr) > 1:
    if cntArr[0][1] == cntArr[1][1]:
        print(cntArr[1][0])
    else:
        print(cntArr[0][0]);
else:
    print(cntArr[0][0]);

#4.범위
print(numbers[-1]-numbers[0]);