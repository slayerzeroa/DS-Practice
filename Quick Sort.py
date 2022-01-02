# Insertion Sort to use in Quick Sort
def insertion_sort(a):                  # 삽입 정렬
    for i in range(1, len(a)):          # 1~전체 반복 (0은 이미 정렬 되었다 가정)
        for j in range(i, 0, -1):       # i~0까지 -1 반복 (현재 원소가 정렬된 부분에 삽입될 곳을 찾아서)
            if a[j-1] > a[j]:           # 만약 정렬 안된 부분의 맨 왼쪽 원소보다 크면
                a[j], a[j-1] = a[j-1], a[j] # 둘이 위치 변경

CALL_SIZE = 8

# Quick Sort
def qsort(a, low, high):
    if high < low + CALL_SIZE:
        insertion_sort(a)
        return
    else:
        pivot = partition(a, low, high)     # 피벗을 기준으로 분할
        qsort(a, low, pivot-1)      # 앞/뒷부분 재귀호출
        qsort(a, pivot+1, high)     # 앞/뒷부분 재귀호출

def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:     # a[i]가 피벗보다 작으면 i를 1 증가
            i += 1
        while j > pivot and a[j] > a[pivot]:    # a[j]가 피벗보다 크면 j를 1 감소
            j -= 1
        if j <= i:  # 루프 중단
            break
        a[i], a[j] = a[j], a[i]     # a[i]와 a[j] 교환
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot] # a[j]와 피벗 교환
    return j    # 피벗 인덱스

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', a)
qsort(a, 0, len(a)-1)       # 퀵정렬 호출
print('정렬 후:\t', a)