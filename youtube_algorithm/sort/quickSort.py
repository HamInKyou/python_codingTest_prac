array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start;
    left= start +1;
    right = end;
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1; #pivot보다 큰거 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1; #pivot보다 작은거 찾을 때까지 반복
        if(left > right): #엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right]; #작은 데이터와 피벗 교체
        else: #엇갈리지 않았다면
            array[left], array[right] = array[right], array[left]; #큰거와 작은거 교체
    #분할 이후 피봇을 기준으로 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1);
    quick_sort(array, right+1, end);

quick_sort(array, 0, len(array)-1);
print(array);


#파이썬의 장점을 살린다면
def quick_sort_advanced(array):
    if len(array) <= 1: #리스트가 하나 이하의 원소만을 담고 있다면 종료
        return array;
    pivot = array[0]; #피벗은 첫번째 원소
    tail = array[1:]; #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]; #왼쪽에 피벗보다 작은 것만 남기기
    right_side = [x for x in tail if x > pivot]; #오른쪽에 피벗보다 큰것만 남기기

    return quick_sort_advanced(left_side) + [pivot] + quick_sort_advanced(right_side);

print(quick_sort_advanced(array));