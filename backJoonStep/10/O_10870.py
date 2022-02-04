import sys;
input = sys.stdin.readline;

def fibonacci(num):
    if num > 1:
        return fibonacci(num-1)+fibonacci(num-2);
    elif num == 1:
        return 1;
    elif num == 0:
        return 0;

n = int(input());
print(fibonacci(n))