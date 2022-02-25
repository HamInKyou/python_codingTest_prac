import sys;
from bisect import bisect_left, bisect_right;
input = sys.stdin.readline;

n, x = map(int, input().split());
arr = list(map(int, input().split()));

start = bisect_left(arr, x);
end = bisect_right(arr, x);
result = end - start;
if result == 0:
    print(-1);
else:
    print(result);