import sys;
input = sys.stdin.readline;

n = int(input());
arr = [];
for _ in range(n):
    arr.append(int(input()));

def selection_sort(arr):
    for i in range(len(arr)):
        minIndex = i;
        for j in range(i, len(arr)):
            if(arr[minIndex] > arr[j]):
                minIndex = j;
        arr[i],arr[minIndex] = arr[minIndex],arr[i];

selection_sort(arr);
for num in arr:
    print(num);