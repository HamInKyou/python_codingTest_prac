import sys;
input = sys.stdin.readline;

n = int(input());

stack = [];
result = [];

flag = 0;
curNum = 1;
for _ in range(n):
    targetNum = int(input());
    while curNum <= targetNum:
        stack.append(curNum);
        result.append('+');
        curNum += 1;
    if stack[-1] == targetNum:
        stack.pop();
        result.append('-');
    else:
        flag = 1;
        break;

if flag:
     print("NO");
else:
    for c in result:
        print(c);
