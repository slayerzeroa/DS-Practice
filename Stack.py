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

def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in '+-*/':
            val2 = s.pop()
            val1 = s.pop()
            if(token == '+'):
                s.push(val1 + val2)
            elif(token == '-'):
                s.push(val1 - val2)
            elif(token == '*'):
                s.push(val1 * val2)
            elif(token == '/'):
                s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()

def precedence(op): #연산 우선순위
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1

def Infix2Postfix(expr): #expr: 입력 리스트(중위 표기식)
    s = Stack()
    output = []
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op=='(':
                    break;
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if(precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output


infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
print(postfix1)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)
print('중위표기:', infix1)
print('후위표기:', postfix1)
print('계산결과:', result1, end='\n\n')
print('중위표기:', infix2)
print('후위표기:', postfix2)
print('계산결과:', result2)

infix3 = ['(','9','/','3','+','5',')','/','2','-','(','3','*','2',')']
postfix3 = Infix2Postfix(infix3)
print(postfix3)
result3 = evalPostfix(postfix3)
print(result3)