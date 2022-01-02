class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self): # 공백 상태 검사
        return self.front == None

    def clear(self): # 초기화
        self.front = self.rear = None

    def size(self):  # 스택의 항목 수 계산
        node = self.front  # 시작 노드
        count = 0
        while not node == None:  # node가 None이 아닐 때 까지
            node = node.next  # 다음 노드로 이동
            count += 1  # count 증가
        return count  # count 반환

    def display(self, msg = 'LinkedStack : '):
        print(msg, end='')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.next
        print()

    def addFront(self, item):
        node = DNode(item, None, self.front) # Step 1
        if (self.isEmpty()): # 공백이면
            self.front = self.rear = node # front와 rear 모두 node
        else: # 공백이 아니면
            self.front.prev = node # Step 2
            self.front = node # Step 3

    def addRear(self, item):
        node = DNode(item, self.rear, None) # Step 1
        if(self.isEmpty()): # 공백이면
            self.front = self.rear = None # front와 rear 모두 node
        else: # 공백이 아니면
            self.rear.next = node # Step 2
            self.rear = node # Step 3

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data # Step 1
            self.front = self.front.next # Step 2
            if self.front==None: # 노드가 하나뿐이면
                self.rear = None # rear도 None으로 설정
            else:
                self.front.prev = None # Step 3
            return data # Step 4

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data # Step 1
            self.rear = self.rear.prev # Step 2
            if self.rear == None: # 노드가 하나뿐이면
                self.front = None # front도 None으로 설정
            else:
                self.rear.next = None # Step 3
            return data # Step 4


dq = DoublyLinkedDeque() # 연결된 덱
for i in range(9):
    if i%2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.display()
for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deleteRear()
dq.display()
for i in range(9, 14):
    dq.addFront(i)
dq.display()