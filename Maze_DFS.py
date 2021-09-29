map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]
MAZE_SIZE = 6

class Stack:
    def __init__(self): #생성자
        self.top = [] #top이 클래스의 멤버 변수

    def isEmpty(self): #빈 리스트 확인 함수
        return len(self.top) == 0
    def size(self):
        return len(self.top)
    def clear(self):
        self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

def isValidPos(x, y):
    if x<0 or y<0 or x>= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def DFS(): #깊이우선탐색 함수
    stack = Stack() #사용할 스택 객체 준비
    stack.push((0,1)) #시작위치 삽입, (0,1)은 튜플
    print('DFS: ')

    while not stack.isEmpty(): # 공백이 아닌동안
        here = stack.pop() # 항목을 꺼냄(pop)
        print(here, end='->')
        (x, y) = here
        if map[y][x] == 'x': #출구이면 탐색 성공. True 반환
            return True
        else:
            map[y][x] = '.' #현재위치를 지나왔다고 '.'표시
            #4방향의 이웃을 검사해 갈 수 있으면 스택에 삽입
            if isValidPos(x, y-1):
                stack.push((x, y-1))
            if isValidPos(x, y+1):
                stack.push((x, y+1))
            if isValidPos(x-1, y):
                stack.push((x-1, y))
            if isValidPos(x+1, y):
                stack.push((x+1, y))
        print(' 현재 스택: ', stack.top) # 현재 스택 내용 출력
    return False #탐색 실패, False 반환

result = DFS()
if result:
    print(' ---> 미로탐색 성공')
else:
    print(' ---> 미로탐색 실패')