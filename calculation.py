items = [] # 리스트 항목 저장을 위한 파이썬 리스트
def insert(pos, elem): # pos 위치에 새로운 요소 item을 삽입한다.
    items.insert(pos,elem) # 파이썬 리스트 클래스의 insert 연산

def delete(pos): # pos 위치에 있는 요소를 꺼내고 반환한다.
    return items.pop(pos) # 파이썬 리스트 클래스의 pop 연산

def getEntry(pos):
    return items[pos] # pos번째 항목 반환

def isEmpty():
    return len(items) == 0 # 크기가 0이면 True 아니면 False

def size():
    return len(items) #리스트의 크기 반환, len()함수 이용

def clear():
    global items
    items = [] #items를 초기화 --> 오류

def find(item):
    return items.index(item) # 탐색 후 인덱스 반환

def replace(pos, elem):
    items[pos] = elem # pos번째 항목 변경

def sort():
    items.sort() # 정렬(sort 메소드 이용)

def merge(lst):
    items.extend(lst) # 병합(확장)

def display(msg='ArrayList:'):
    print(msg, size(), items)  # 메세지 + 크기 + 배열내용 출력


insert(0, 6)
clear()
print(items)


def myLineEditor(): # 라인 편집기 주 함수
    list = []# 리스트 객체 생성
    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=>")

    if command == 'i': #삽입 연산
        pos = int(input(" 입력행 번호: ")) #삽입할 행 번호 입력
        str = input(" 입력행 내용: ") # 삽입할 행 내용 입력
        list.insert(pos,str) #insert 메소드로 삽입
    elif command == 'd': # 행 삭제
        pos = int(input(" 삭제행 번호: ")) # 삭제할 행 번호 입력
        list.delete(pos) # delete 메소드로 삭제
    elif command == 'r': #행 내용 변경
        pos = int(input(" 변경행 번호: ")) # 변경할 행 번호 입력
        str = input(" 변경행 내용: ") # 변경할 행 내용 입력
        list.replace(pos, str) # replace로 변경
    elif command == 'q':
        return
    elif command == 'p':
        print('Line Editor')
        for line in range (list.size()):
            print('[%2d]' %line, end='')
            print(list.getEntry(line))
        print()
    elif command == 'l':
        filename = 'test.txt'
        infile = open(filename, "r")
        lines = infile.readline()
        for line in lines:
            list.insert(list.size(), line.rstrip('\n'))
        infile.close()
    elif command == 's':
        filename == 'test.txt'
        outfile = open(filename, 'w')
        for i in range(list.size()):
            outfile.write(list.getItem(i)+'\n')
        outfile.close()
myLineEditor()