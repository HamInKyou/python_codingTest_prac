import sys;
input = sys.stdin.readline;

num = input().rstrip();
numArr = list(num);
numArr.sort(reverse=True);
print("".join(numArr))