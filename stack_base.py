top = []

# 스택의 함수 버전
def isEmpty():
    return len(top) == 0 # len(top) == 0의 계산 결과가 True/False

def push(item):
    top.append(item) # 리스트의 맨 뒤에 item을 추가함

def pop():
    if not isEmpty(): # 공백상태가 아니면
        return top.pop(-1) # 리스트의 맨 뒤에서 항목을 하나 꺼내고 반환

def peek(): # 맨 위의 항목을 삭제하지 않고 반환
    if not isEmpty(): # 공백상태가 아니면
        return top[-1] # 맨 뒷 항목을 반환 (삭제하지 않음)

def size(): # 스택의 크기
    return len(top)

def clear():
    global top # 전역변수를 지정함
    top = [] # 초기화


for i in range(1, 6):
    push(i)
print('push 5회: ', top)
print('pop() -->', pop())
print('pop() -->', pop())
print('pop 2회: ', top)


# 스택의 클래스 버전
class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
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

odd = Stack()
even = Stack()
for i in range(10):
    if i%2 == 0:
        even.push(i)
    else:
        odd.push(i)

print('스택 even push 5회: ', even.top)
print('스택 odd push 5회: ', odd.top)
print('스택 even peek: ', even.peek())
print('스택 odd peek: ', odd.peek())
for _ in range(2):
    even.pop()
for _ in range(3):
    odd.pop()
print('스택 even pop: ', even.pop())
print('스택 odd pop: ', odd.pop())


# 괄호 검사 알고리즘
def checkBrackets(statement):
    stack = Stack()
    for ch in statement: # 문자열의 각 문자에 대해
        if ch in ('{', '[', '('): # in '{[('도 동일하게 동작함
            stack.push(ch)
        elif ch in ('}', ']', ')'): # in '}])'도 동일하게 동작함
            if stack.isEmpty():
                return False # 조건 2 위반
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "("):
                    return False
    return stack.isEmpty() # False이면 조건 1 위반

str = ("{A[(i+1)] = 0;}", "if((i==0)&&(j==0)", "A{[(i+1)]}")

for s in str:
    m = checkBrackets(s)
    print(s,"--->",m)