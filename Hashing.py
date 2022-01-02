class LinearProbing: # 선형 조사
    def __init__(self, size):       # 객체 생성자
        self.M = size               # 테이블 크기 M
        self.a = [None] * size      # 해시테이블 a
        self.d = [None] * size      # 데이터 저장용 d

    def hash(self, key):
        return key % self.M         # 나눗셈 해시 함수

    def put(self, key, data):       # 삽입 연산
        initial_position = self.hash(key)   # 초기 위치
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:   # 빈 곳 발견
                self.a[i] = key     # key는 해시테이블에
                self.d[i] = data    # data는 리스트 d에 저장
                return
            if self.a[i] == key:    # key가 이미 해시테이블에 있으면
                self.d[i] = data    # data만 갱신해준다
                return
            j += 1
            i = (initial_position + j) % self.M     # 다음 원소 검사를 위해
            if i == initial_position:   # 다음위치가 초기 위치와 같으면
                break                   # 루프 벗어나기(저장 실패)

    def get(self, key): #탐색 연산
        initial_position = self.hash(key)   # 초기 위치
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]    # 탐색 성공
            i = (initial_position + j) % self.M     # 다음 원소 검사를 위해
            j += 1
            if i == initial_position:
                return None # 탐색 실패
        return None         # 탐색 실패

    def print_table(self):  # 해시테이블 출력
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ', end='')
        print()

if __name__ == '__main__':
    t = LinearProbing(13)
    # 항목 삽입
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    # 탐색 및 테이블 출력
    print('선형조사 탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t.get(63))
    print('해시테이블 : ')
    t.print_table()

class QuadProbing: # 2차 조사
    def __init__(self, size):       # 객체 생성자
        self.M = size               # 테이블 크기 M
        self.a = [None] * size      # 해시테이블 a
        self.d = [None] * size      # 데이터 저장용 d
        self.N = 0                  # 저장된 항목 수 N

    def hash(self, key):            # 나눗셈 해시함수
        return key % self.M         # 나눗셈 해시함수

    def put(self, key, data):       # 삽입 연산
        iniitial_position = self.hash(key)  # 초기 위치
        i = iniitial_position
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (iniitial_position + j*j) % self.M
            if self.N > self.M: # 만약 저장된 항목 수가 테이블 크기보다 크면
                break           # 저장실패

    def get(self, key):     # 탐색 연산
        initial_position = self.hash(key)   # 초기 위치
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]    # 탐색 성공
            i = (initial_position + j*j) % self.M
            j += 1
        return None     # 탐색 실패

    def print_table(self):  # 해시테이블 출력
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ', end='')
        print()


if __name__ == '__main__':
    t = QuadProbing(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    # 탐색 및 테이블 출력
    print('이차조사 탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t.get(63))
    print('해시테이블 : ')
    t.print_table()

import random       #random 패키지 불러오기
class RandProbing:  # 랜덤 조사
    def __init__(self, size):       # 객체 생성자
        self.M = size               # 테이블 크기 M
        self.a = [None] * size      # 해시테이블 a
        self.d = [None] * size      # 데이터 저장용 d
        self.N = 0                  # 저장된 항목 수 N

    def hash(self, key):            # 나눗셈 해시함수
        return key % self.M         # 나눗셈 해시함수

    def put(self, key, data):       # 삽입 연산
        initial_position = self.hash(key)   # 초기 위치
        i = initial_position
        random.seed(1000)           # 난수 생성 초기값
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j = random.randint(1, 99)    # 난수 크기 범위 지정
            i = (initial_position + j) % self.M  # 다음 원소 검사를 위해
            if self.N > self.M:
                break

    def get(self, key):     # 탐색 연산
        initial_position = self.hash(key)   # 초기 위치
        i = initial_position
        random.seed(1000)               # 저장할 때와 동일한 난수 생성 초기값
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]    # 탐색 성공
            i = (initial_position + random.randint(1, 99)) % self.M
        return None     # 탐색 실패

    def print_table(self):  # 해시테이블 출력
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ', end='')
        print()

if __name__ == '__main__':
    t = RandProbing(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    # 탐색 및 테이블 출력
    print('랜덤조사 탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t.get(63))
    print('해시테이블 : ')
    t.print_table()

class DoubleHashing:    # 이중 해싱
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0  # 항목 수

    def hash(self, key):
        return key % self.M

    def put(self, key, data):   # 삽입 연산
        initial_position = self.hash(key)
        i = initial_position
        d = 7 - (key % 7)
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j*d) % self.M
            if self.N > self.M:
                break

    def get(self, key): # 탐색 연산
        initial_position = self.hash(key)
        i = initial_position
        d = 7 - (key % 7)
        j = 0
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            j += 1
            i =(initial_position + j*d) % self.M
        return None

    def print_table(self):  # 해시테이블 출력
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ', end='')
        print()

if __name__ == '__main__':
    t = DoubleHashing(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    # 탐색 및 테이블 출력
    print('이중해싱 탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t.get(63))
    print('해시테이블 : ')
    t.print_table()