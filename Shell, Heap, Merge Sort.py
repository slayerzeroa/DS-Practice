# Shell Sort
def shell_sort(a):
    h = 4           # 3x+1 간격 : 1, 4, 13, 40, 121, ... 중에서 4와 1만 사용
    while h >= 1:
        for i in range(h, len(a)):  # h-정렬 수행
            j = i
            while j >= h and a[j] < a[j-h]:     # 각 그룹에 대해 삽입 정렬 수행
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h //= 3     # 다음 h값 계산

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', end='')
print(a)
shell_sort(a)
print('정렬 후:\t', end='')
print(a)


# Heap Sort
def downheap(i, size):      # 루트로 올라온 키에 대해 힙속성을 회복시킴
    while 2*i <= size:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k += 1
        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k

def create_heap(a):         # 정렬하기 전에 최대힙 만들기
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2+1)):
        downheap(i, hsize)


def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1]     # 루트와 힙의 마지막 항목 교환
        downheap(1, N-1)
        N -= 1              # 힙 크기 1 감소

a = [-1, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', end='')
print(a)
create_heap(a)      # 힙 만들기
print('최대힙:\t', end='')
print(a)
heap_sort(a)
print('정렬 후:\t', end='')
print(a)


def merge(a, b, low, mid, high):
    i = low
    j = mid+1
    for k in range(low, high+1):        # a의 앞/뒷부분 합병하여 b에 저장
        if i > mid:
            b[k] = a[j]                 # a의 앞부분이 먼저 소진되어 뒷부분 b로 복사
            j += 1
        elif j > high:
            b[k] = a[i]                 # a의 뒷부분이 먼저 소진되어 앞부분 b로 복사
            i += 1
        elif a[j] < a[i]:
            b[k] = a[j]                 # a[j]가 승자
            j += 1
        else:
            b[k] = a[i]                 # a[i]가 승자
            i += 1
    for k in range(low, high+1):
        a[k] = b[k]                     # b를 a로 복사

def merge_sort(a, b, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2       # 중간 인덱스
    merge_sort(a, b, low, mid)          # 앞/뒷부분 재귀호출
    merge_sort(a, b, mid + 1, high)     # 앞/뒷부분 재귀호출
    merge(a, b, low, mid, high)         # 정렬된 앞/뒷부분 합병

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
b = [None] * len(a)     # 보조 리스트
print('정렬 전:\t', end='')
print(a)
merge_sort(a, b, 0, len(a)-1)       # 합볍정렬 호출
print('정렬 후:\t', end='')
print(a)