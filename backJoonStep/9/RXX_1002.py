import sys;
input = sys.stdin.readline;

t = int(input());

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split());

    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5;
    if distance > r1 + r2:
        print(0);
    elif distance == r1 + r2:
        print(1);
    else:
        rSub = max(r1,r2) - min(r1,r2)
        if distance < rSub:
            print(0);
        elif distance == rSub:
            if distance == 0 and rSub == 0:
                print(-1);
            else:
                print(1);
        else :
            print(2);