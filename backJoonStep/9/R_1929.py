import sys;
input = sys.stdin.readline;

m,n = map(int, input().split());


#에라토스테네스의 체를 이용하여 소수 배열 구하기
arr = list(range(n+1));

for i in range(2, int(n**(1/2)+1)):
    if arr[i] > 0:
        j = 2;
        while i*j <= n:
            arr[i*j] = 0;
            j += 1;

#print(arr[2:]); -> 얘가 소수들 담겨져있는 배열 (지워진애들 0으로 포함)

for i in range(m,n+1):
    if arr[i] > 0 and i > 1:
        print(i)

