import sys;
input = sys.stdin.readline;

def factorial(number):
    return number*factorial(number-1) if number>1 else 1;

n = int(input());
print(factorial(n));
