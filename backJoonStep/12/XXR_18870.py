import sys;
input = sys.stdin.readline;

n = int(input());
arr = list(map(int, input().split()));

# 첫번째 시간초과
# for num in arr:
#     count = 0;
#     for i in arr:
#         if num > i:
#             count+=1;
#     print(count, end=" ")

# 두번째 시간초과
# sortedArr = sorted(arr);
# for num in arr:
#     val = sortedArr.index(num);
#     print(val, end=" ")

sortedArr = sorted(list(set(arr)));
numDic = { sortedArr[i] : i for i in range(len(sortedArr))}; #dic꼴로 저장하면서 탐색 속도 O(1)로 줄일 수 있었음!

for num in arr:
    print(numDic[num], end=" ")