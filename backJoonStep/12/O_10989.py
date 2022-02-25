import sys;
input = sys.stdin.readline;

MAX = 10000;
n = int(input());
counter = [0]*(MAX+1);

for _ in range(n):
    num = int(input())
    counter[num] += 1;

for num in range(1, MAX+1):
    if counter[num] > 0:
        for _ in range(counter[num]):
            print(num);