# Queue
MAX_QSIZE = 10   # 원형 큐의 크기

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

q = CircularQueue()
for i in range(8):
    q.enqueue(i)
q.display()
for i in range(5):
    q.dequeue()
q.display()
for i in range (8, 14):
    q.enqueue(i)
q.display()


# 너비 우선 탐색
def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def BFS(): #너비우선탐색 함수
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS : ') # 출력을 BFS로 변경

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x, y = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1):
                que.enqueue((x, y-1))
            if isValidPos(x, y+1):
                que.enqueue((x, y+1))
            if isValidPos(x-1, y):
                que.enqueue((x-1, y))
            if isValidPos(x+1, y):
                que.enqueue((x+1, y))

map = [['1','1','1','1','1','1'],
       ['e','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']]

MAZE_SIZE = 6

result = BFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')

import queue
Q = queue.Queue(maxsize=20)

for v in range(1,10):
    Q.put(v)
print('큐의 내용', end='')
for _ in range(1,10):
    print(Q.get(), end=' ')
print()