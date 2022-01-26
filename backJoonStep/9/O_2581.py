import sys;
input = sys.stdin.readline;

m = int(input());
n = int(input());

def checkSosu(num):
    if num < 2:
        return False;
    else:
        for i in range(2, int(num**(1/2))+1):
            if num%i == 0:
                return False;
        return True;

sum = 0;
min = 0;

for i in range(m, n+1):
    if checkSosu(i):
        if min == 0:
            min = i;
        sum += i;

if sum > 0:
    print(sum);
    print(min);
else:
    print(-1)
            
