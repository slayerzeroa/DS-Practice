# LSD Sort

def lsd_sort(a):
    WIDTH = 3           # 입력 : 3개의 문자로 된 스트링
    N = len(a)
    R = 128             # 문자 종류 수(UTF-8, ASCII)
    temp = [None] * N
    for d in reversed(range(WIDTH)):    # 2, 1, 0 순으로
        count = [0] * (R+1)
        for i in range(N):
            count[ord(a[i][d])+1] += 1  # 빈도수 계산
        for j in range(1, R):
            count[j] += count[j-1]      # temp에 저장할 시작 인덱스 계산
        for i in range(N):              # d번째 문자를 기준으로 각 a[i]를 적절한 temp 원소로 복사
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] += 1
        for i in range(N):              # temp를 a로 복사
            a[i] = temp[i]
        print('%d번째 문자:\t ' % d, end='')
        for x in a: print(x, ' ', end='')
        print()
a = ['ICN', 'SIN', 'LAX', 'FRA', 'SFO', 'ROM', 'HKG', 'TLV', 'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BER', 'MOW']
print('정렬 전:\t', end='')
for x in a: print(x, ' ', end='')
print()
lsd_sort(a)

'''
# MSD Sort
def msd_sort(a):
    WIDTH = 3           # 입력 : 3개의 문자로 된 스트링
    N = len(a)
    R = 128             # 문자 종류 수(UTF-8, ASCII)
    temp = [None] * N
    for d in range(WIDTH):    # 0, 1, 2 순으로
        count = [0] * (R+1)
        for i in range(N):
            count[ord(a[i][d])+1] += 1  # 빈도수 계산
        for j in range(1, R):
            count[j] += count[j-1]      # temp에 저장할 시작 인덱스 계산
        for i in range(N):              # d번째 문자를 기준으로 각 a[i]를 적절한 temp 원소로 복사
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] += 1
        for i in range(N):              # temp를 a로 복사
            a[i] = temp[i]
        print('%d번째 문자:\t ' % d, end='')
        for x in a: print(x, ' ', end='')
        print()
a = ['ICN', 'SIN', 'LAX', 'FRA', 'SFO', 'ROM', 'HKG', 'TLV', 'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BER', 'MOW']
print('정렬 전:\t', end='')
for x in a: print(x, ' ', end='')
print()
msd_sort(a)
'''