import sys;
input = sys.stdin.readline;

xArr = []
yArr = []
for _ in range(3):
    x, y = map(int, input().split());
    xArr.append(x);
    yArr.append(y);

newX = 0
newY = 0
for i in range(3):
    if xArr.count(xArr[i]) == 1:
        newX = xArr[i];
    if yArr.count(yArr[i]) == 1:
        newY = yArr[i];

print(newX, newY)