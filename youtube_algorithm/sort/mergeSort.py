array = [ 7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

def merge(leftArr, rightArr):
    resultArr = [];
    l = r = 0;
    while l < len(leftArr) and r < len(rightArr): #왼쪽이든 오른쪽이든 어느하나 다 꺼낼 때까지.
        if leftArr[l] < rightArr[r]: #왼쪽배열에 있는애가 작으면 왼쪽걸 꺼내기
            resultArr.append(leftArr[l]);
            l += 1;
        else:
            resultArr.append(rightArr[r]); #오른쪽배열에 있는 애가 작으면 오른쪽걸 꺼내기
            r += 1;
    if l < len(leftArr):
        resultArr += leftArr[l:];  #왼쪽 배열 남았다면 남은애들 싹 다 뒤에 붙이기
    elif r < len(rightArr):
        resultArr += rightArr[r:]; #오른쪽 배열 남았다면 남은애들 싹 다 뒤에 붙이기
    return resultArr;

def merge_sort(arr):
    if len(arr) <= 1:
        return arr;
    mid = len(arr) // 2; #중간 기준
    leftArr = arr[:mid]; #왼쪽
    rightArr = arr[mid:] #오른쪽
    leftArr = merge_sort(leftArr); #왼쪽 정렬
    rightArr = merge_sort(rightArr); #오른쪽 정렬
    return merge(leftArr, rightArr);

array = merge_sort(array);
print(array);