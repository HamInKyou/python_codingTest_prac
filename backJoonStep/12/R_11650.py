import sys;
input = sys.stdin.readline;

n = int(input());

arr = [];
for _ in range(n):
    x, y = map(int, input().split());
    arr.append([x,y]);

# 이건 시간초과한 답변
# for i in range(n-1):
#     minIdx = i;
#     minVal = arr[i];
#     for j in range(i+1, n):
#         if arr[j][0] < minVal[0]:
#             minIdx = j;
#             minVal = arr[j];
#         elif arr[j][0] == minVal[0] and arr[j][1] < minVal[1]:
#             minIdx = j;
#             minVal = arr[j];
#     arr[i], arr[minIdx] = arr[minIdx], arr[i];

# for pair in arr:
#     x,y = pair;
#     print(x,y)

arr.sort(key=lambda x: (x[0],x[1]));
for pair in arr:
    x,y = pair;
    print(x,y)