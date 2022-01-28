import sys;
input = sys.stdin.readline;

x, y, w, h = map(int,input().split());

#x축 판별
xDistance = min(w-x, x);
#Y축 판별
yDistance = min(h-y, y);
#최소값
minDistance = min(xDistance,yDistance);
print(minDistance)

