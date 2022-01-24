import sys;
input = sys.stdin.readline;

testCase = int(input());
for _ in range(testCase):
    h, w, n = map(int, input().split());
    x = h if n%h == 0 else n%h ;
    y = (n//h) if n%h == 0 else (n//h)+1
    roomNum = (x*100) + y
    print(roomNum)
