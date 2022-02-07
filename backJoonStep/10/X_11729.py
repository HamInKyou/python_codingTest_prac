import sys;
input = sys.stdin.readline;

result = [];

def hanoi(n, start, end):
    if n == 1:
        result.append(f"{start} {end}")
        return;

    towers = {1,2,3}
    mid = (towers - {start, end}).pop();

    hanoi(n-1, start, mid);
    result.append(f"{start} {end}")
    hanoi(n-1, mid, end);
    
n = int(input());
hanoi(n, 1,3);
print(len(result));
for move in result:
    print(move)