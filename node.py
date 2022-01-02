class Node: # 단순연결리스트를 위한 노드 클래스
    def __init__(self, elem, link=None): # 생성자, 디폴트 인수 사용
        self.data = elem    # 데이터 멤버 생성 및 초기화
        self.link = link    # 링크 생성 및 초기화

class LinkedStack: # 연결된 스택 클래스
    def __init__(self): # 생성자
        self.top = None # top 생성 및 초기화

    def isEmpty(self): # 공백상태 검사
        return self.top == None

    def clear(self): # 스택 초기화
        self.top = None

    def push(self, item): # 연결된 스택의 삽입연산
        n = Node(item, self.top) # Step1 + Step2
        self.top = n # Step3

    def pop(self): # 연결된 스택의 삭제연산
        if not self.isEmpty(): # 공백이 아니면
            n = self.top # Step1
            self.top = n.link # Step2
            return n.data # Step3

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def size(self): # 스택의 항목 수 계산
        node = self.top # 시작 노드
        count = 0
        while not node == None: # node가 None이 아닐 때 까지
            node = node.link # 다음 노드로 이동
            count += 1 # count 증가
        return count # count 반환

    def display(self, msg = 'LinkedStack : '):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

odd = LinkedStack()
even = LinkedStack()
for i in range(10):
    if i%2 == 0:
        even.push(i)
    else:
        odd.push(i)
even.display('스택 even push 5회 : ')
odd.display('스택 odd push 5회 : ')
print('스택 even peek : ', even.peek())
print('스택 odd peek : ', odd.peek())
for _ in range(2):
    even.pop()
for _ in range(3):
    odd.pop()
even.display('스택 even pop 2회 : ')
odd.display('스택 odd pop 3회 : ')


class LinkedList: # 연결된 리스트 클래스
    def __init__(self):
        self.head = None

    def isEmpty(self): # 공백검사 검사
        return self.head == None

    def clear(self): # 리스트 초기화
        self.head = None

    def size(self):
        node = self.head # 시작 노드
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end = ' ')
            node = node.link
        print()

    def getNode(self, pos): # pos 번째 노드 반환
        if pos < 0:
            return None
        node = self.head # node는 head부터 시작
        while pos > 0 and node != None: # pos번 반복
            node = node.link # node를 다음 node로 이동
            pos -= 1 # 남은 반복 횟수 줄임
        return node # 최종 노드 반환

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None:
            node.data = elem

    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.link
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

s = LinkedList()
s.display('단순연결리스트로 구현한 리스트(초기상태) : ')
s.insert(0, 10);s.insert(0, 20);s.insert(1, 30)
s.insert(s.size(), 40); s.insert(2, 50)
s.display('단순연결리스트로 구현한 리스트(삽입x5) : ')
s.replace(2, 90)
s.display('단순연결리스트로 구현한 리스트(교체x1) : ')
s.delete(2); s.delete(s.size() - 1); s.delete(0)
s.display('단순연결리스트로 구현한 리스트(삭제x3) : ')
s.clear()
s.display('단순연결리스트로 구현한 리스트(정리후) : ')


class CircularLinkedQueue:
    def __init__(self): # 생성자 함수
        self.tail = None # tail : 유일한 데이터

    def isEmpty(self): # 공백상태 검사
        return self.tail == None

    def clear(self): # 큐 초기화
        self.tail = None

    def peek(self): # peek 연산
        if not self.isEmpty(): # 공백이 아니면
            return self.tail.link.data # front의 data를 반환

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def size(self):
        if self.isEmpty(): # 공백이면 0 반환
            return 0
        else: # 공백 아니면
            count = 1 # count는 최소 1
            node = self.tail.link # node는 front부터 출발
            while not node == self.tail: # node가 rear가 아닌 동안
                node = node.link # 이동
                count += 1 # count 증가
            return count # 최종 count 반환

    def display(self, msg='CircularLinkedQueue : '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end = ' ')
        print()

q=CircularLinkedQueue()
for i in range(8):
    q.enqueue(i)
q.display()
for i in range(5):
    q.dequeue()
q.display()
for i in range(8, 14):
    q.enqueue(i)
q.display()


n = range(10)
sum = 0
for i in n:
    for j in n:
        sum += 1