# Selection Sort
def selection_sort(a):                  # 선택 정렬
    for i in range(0, len(a)-1):        # 전체 길이의 -1만큼 반복 (마지막 요소는 정렬 필요 X)
        minimum = i                     # 최소 설정
        for j in range(i, len(a)):      # i~끝 반복
            if a[minimum] > a[j]:       # 만약 minimum 요소가 j 요소보다 크면
                minimum = j             # j를 minimum으로 변경한다
        a[i], a[minimum] = a[minimum], a[i] # minimum이 j로 바뀌었으면 j와 i의 위치변경, 아니면 그대로


a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', end='')
print(a)
selection_sort(a)
print('정렬 후:\t', end='')
print(a)



# Insertion Sort
def insertion_sort(a):                  # 삽입 정렬
    for i in range(1, len(a)):          # 1~전체 반복 (0은 이미 정렬 되었다 가정)
        for j in range(i, 0, -1):       # i~0까지 -1 반복 (현재 원소가 정렬된 부분에 삽입될 곳을 찾아서)
            if a[j-1] > a[j]:           # 만약 정렬 안된 부분의 맨 왼쪽 원소보다 크면
                a[j], a[j-1] = a[j-1], a[j] # 둘이 위치 변경

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', end='')
print(a)
insertion_sort(a)
print('정렬 후:\t', end='')
print(a)