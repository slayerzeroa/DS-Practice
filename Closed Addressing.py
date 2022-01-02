class Chaining:
    class Node:
        def __init__(self, key, data, link):    # 노드 객체 생성자
            self.key = key
            self.data = data
            self.next = link

    def __init__(self, size):       # Chaining 객체 생성자
        self.M = size
        self.a = [None] * size      # 해시테이블 a

    def hash(self, key):            # 나눗셈 해시함수
        return key % self.M

    def put(self, key, data):       # 삽입 연산
        i = self.hash(key)
        p = self.a[i]
        while p!= None:
            if key == p.key:        # key가 있으면 data 갱신
                p.data = data
                return
            p = p.next
        self.a[i] = self.Node(key, data, self.a[i]) # 새 노드 생성, 단순연결리스트 맨 앞에 삽입

    def get(self, key):             # 탐색 연산
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:         # 탐색 성공
                return p.data
            p = p.next
        return None                 # 탐색 실패

    def print_table(self):          # 테이블 출력
        for i in range(self.M):
            print('%2d' % (i), end = '')
            p = self.a[i];
            while p != None:
                print('-->[',p.key,',',p.data,']', end ='')
                p = p.next
            print()

if __name__ == '__main__':
    t = Chaining(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    # 탐색 및 테이블 출력
    print('Chaining 탐색 결과:')
    print('해시테이블 : ')
    t.print_table()


# 빠꾸기 해싱 알고리즘
'''
[1]    key = new_key
[2]    h(key) = i를 계산하여, htable[i]에 key를 저장
[3]    if key가 저장된 원소가 비어 있으면:
            삽입을 종료
[4]    else: // 키가 저장되면서 그 자리에 있던 키를 쫒아낸 경우
            key 때문에 쫒겨난 키를 old_key라고 하자
[5]      if old_key가 있던 테이블이 htable이면:
            d(old_key)=j를 계산하여, dtable[j]에 old_key를 저장
[6]      else: // old_key가 있었던 테이블이 dtable이면
            h(old_key)=j를 계산하여, htable[j]에 old_key를 저장
[7]      key = old_key, go to step[3] 
'''