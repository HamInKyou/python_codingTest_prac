import sys;
input = sys.stdin.readline;

def sosuArrMaker(num):
    arr = list(range(num+1));
    for i in range(2, num+1):
        if i > 0:
            j = 2;
            while i * j <= num:
                arr[i*j] = 0;
                j+=1;
    
    sosuArr = [ i for i in arr[2:] if i > 0];
    return sosuArr;

sosuArr = sosuArrMaker(123456*2);
while True:
    n = int(input());
    if n == 0:
        break;
    cnt = len([i for i in sosuArr if i > n and i <= 2*n]) 
    print(cnt)
