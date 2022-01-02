MAX_QSIZE = 20

class CircularQueue:
    def __init__(self): #CircularQueue 생성자
        self.front = 0 # 큐의 전단 위치
        self.rear = 0 # 큐의 후단 위치
        self.items = [None] * MAX_QSIZE # 항목 저장용 리스트 [None, ...]

    def isEmpty(self): # 빈 큐 검증
        return self.front == self.rear

    def isFull(self): # 포화 상태 검증
        return self.front == (self.rear+1) % MAX_QSIZE

    def clear(self): # clear
        self.front = self.rear

    def enqueue(self, item): # 삽입
        if not self.isFull(): # 포화 상태가 아니면
            self.rear = (self.rear+1) % MAX_QSIZE # front 회전
            self.items[self.rear] = item

    def dequeue(self): # 삭제
        if not self.isEmpty(): # 공백 상태가 아니면
            self.front = (self.front+1)%MAX_QSIZE # front 회전
            return self.items[self.front] # front 위치의 항목 반환

    def peek(self): # front 항목 출력
        if not self.isEmpty(): # 공백 상태가 아니면
            return self.items[(self.front + 1) % MAX_QSIZE] # 출력

    def size(self): # 큐 사이즈 출력
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self): # 큐 출력
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1] # 슬라이싱
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
            print("[f=%s, r=%d] ==> "%(self.front, self.rear), out)


class CircularDeque(CircularQueue):
    def __init__(self): # CircularDeque의 생성자
        super().__init__() # 부모 클래스의 생성자 호출함

    def addRear(self, item):
        self.enqueue(item) # enqueue 호출

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item): # 전단 삽입
        if not self.isFull():
            self.items[self.front] = item # 항목 저장
            self.front = self.front - 1 # 반시계 방향으로 회전
            if self.front < 0:
                self.front = MAX_QSIZE - 1

    def deleteRear(self): # 후단 삭제
        if not self.isEmpty():
            item = self.items[self.rear] # 항목 복사
            self.rear = self.rear - 1 # 반시계 방향으로 회전
            if self.rear < 0:
                self.rear = MAX_QSIZE - 1
            return item # 항목 반환

    def getRear(self): # 후단 peek
        return self.items[self.rear]


dq = CircularDeque() # 덱 객체 생성. f=r=0
for i in range(9): # i = 0,1,2,...,8
    if i%2 == 0:
        dq.addRear(i) #짝수는 후단에 삽입
    else:
        dq.addFront(i) #홀수는 전단에 삽입
dq.display() #front=6, rear=5
for i in range(2):
    dq.deleteFront() #전단에서 두 번의 삭제: f=8
for i in range(3):
    dq.deleteRear() #후단에서 세 번의 삭제: r=2
dq.display()
for i in range(9, 14):
    dq.addFront(i) # i:9, 10,... 13 : f=3


class PriorityQueue:
    def __init__(self): # 생성자
        self.items = [] # 항목 저장을 위한 리스트

    def isEmpty(self): # 공백 상태 검사
        return len(self.items) == 0

    def size(self): # 전체 항목의 개수
        return len(self.items)

    def clear(self): # 초기화
        self.items = []

    def enqueue(self, item): # 삽입 연산
        self.items.append(item) # 리스트의 맨 뒤에 삽입(O(1))

    def findMaxIndex(self): # 최대 우선순위 항목의 인덱스 반환
        if self.isEmpty():
            return None
        else:
            highest = 0 # 0번을 최대라고 하고
            for i in range(1, self.size()): # 모든 항목에 대해
                if self.items[i] > self.items[highest]:
                    highest = i #최고 우선순위 인덱스 갱신
            return highest # 최고 우선순위 인덱스 반환

    def dequeue(self): # 삭제 연산
        highest = self.findMaxIndex() # 우선순위가 가장 높은 항목
        if highest is not None:
            return self.items.pop(highest) # 리스트에서 꺼내서 반환

    def peek(self): # peek 연산
        highest = self.findMaxIndex() #우선순위가 가장 높은 항목
        if highest is not None:
            return self.items[highest] # 꺼내지 않고 반환

q = PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(53)
q.enqueue(45)
q.enqueue(15)

print("PQueue: ", q.items)
while not q.isEmpty():
    print("Max Priority = ", q.dequeue())

import math
(ox, oy) = (5, 4)
def dist(x, y):
    (dx, dy) = (ox - x, oy - y)
    return math.sqrt(dx*dx + dy*dy)

def isValidPos(x, y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0, 1, -dist(0, 1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end='->')
        x,y,_ = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1):
                q.enqueue((x, y-1, -dist(x, y-1)))
            if isValidPos(x, y+1):
                q.enqueue((x, y+1, -dist(x, y+1)))
            if isValidPos(x-1, y):
                q.enqueue((x-1, y, -dist(x-1, y)))
            if isValidPos(x+1, y):
                q.enqueue((x+1, y, -dist(x+1, y)))
        print('우선순위 큐: ', q.items)
    return False

map = [['1','1','1','1','1','1'],
       ['e','0','0','0','0','1'],
       ['1','0','1','0','1','1'],
       ['1','1,''1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']]

MAZE_SIZE = 6
result = MySmartSearch()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')