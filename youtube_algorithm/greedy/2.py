import sys;
input = sys.stdin.readline;

numStr = input().rstrip();

result = 0;
for num in numStr:
    if int(num) <= 1 or result <= 1:
        result += num;
    else:
        result *= num;

print(result);
