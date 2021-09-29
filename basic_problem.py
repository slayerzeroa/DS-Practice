# LAB 4-2
age = int(input("나이를 입력하시오：　"))

if age >= 15:
    print("본 영화를 보실 수 있습니다.")
else:
    print("본 영화를 보실 수 없습니다.")


# LAB 4-4
year = int(input("연도를 입력하시오：　"))

if year%4 == 0:
    if year%100 != 0:
        print(year,"년은 윤년입니다.")
    elif year%400 == 0:
        print(year, "년은 윤년입니다.")
    else:
        print(year, "년은 윤년이 아닙니다.")
else:
    print(year, "년은 윤년이 아닙니다.")

# LAB 4-5
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 1:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료 되었습니다.")

# LAB 4-7
ID = str(input("아이디를 입력하시오: "))

if ID == "ilovepython":
    print("환영합니다.")
else:
    print("아이디를 찾을 수 없습니다.")

# LAB 4-8
import random
shoot = str(input("어디를 공격하시겠어요?(왼쪽, 중앙, 오른쪽) : "))

com = random.randint(1, 3)

if com == 1:
    com = "왼쪽"
if com == 2:
    com = "중앙"
if com == 3:
    com = "오른쪽"

if shoot == com:
    print("축하합니다!! 공격에 성공하였습니다.")
    print("컴퓨터의 수비위치 : ", com)
else:
    print("안타깝네요.. 공격에 실패하였습니다.")
    print("컴퓨터의 수비위치 : ", com)


# LAB 4-9
import turtle as t

shape = str(input("도형을 입력하시오(사각형, 삼각형, 원) : "))

if shape == "원":
    half = int(input("반지름 길이를 입력하시오 : "))
else:
    width = int(input("가로길이를 입력하시오 : "))
    height = int(input("세로길이를 입력하시오 : "))

t.Turtle()
t.shape("turtle")

if shape == "원":
    t.circle(half)
elif shape == "사각형":
    t.goto(width, 0)
    t.goto(width, height)
    t.goto(0, height)
    t.goto(0, 0)
else: # 샴갹형
    t.goto(width, 0) # 첫번째 꼭지점 좌표
    t.goto(width/2, height) # 두번째 꼭지점 좌표
    t.goto(0, 0) # 세번째 꼭지점 좌표