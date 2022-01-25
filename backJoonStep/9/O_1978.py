import sys;
input = sys.stdin.readline;

def sosuChecker(num):
    if num < 2:
        return False;
    for i in range(2, int(num**(1/2))+1):
        if num%i == 0:
            return False;
    return True;

n = int(input());
arr = list(map(int, input().split()));
    
count = 0
for i in arr:
    count = count+1 if sosuChecker(i) else count;

print(count);
