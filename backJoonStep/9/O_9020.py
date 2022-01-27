import sys;
input = sys.stdin.readline;

MAX = 10000;
sosuArr = [False, False] + [True for _ in range(MAX-1)];

def init_sosuArr():
    for i in range(2, int(MAX**(1/2))+1):
        if sosuArr[i]:
            j = 2;
            while i*j <= MAX:
                sosuArr[i*j] = False;
                j+=1;

init_sosuArr();
t = int(input());

for _ in range(t):
    n = int(input());
    i = n//2;
    while i < n:
        if sosuArr[i]:
            otherNum = n - i;
            if sosuArr[otherNum]:
                break;
        i+=1;
    print(otherNum, i)
