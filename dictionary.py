#1
EngDic = {"apple":"사과", "orange":"오렌지", "strawberry":"딸기"}
print(EngDic["apple"])

#2
MyData = {"이름":"유대명", "성별":"남성", "키":"188", "몸무게":"82"}
print(MyData["이름"])

#3
EngDic = {"check":["검사하다", "조사하다"], "assign":["할당하다", "배정하다"],
          "involved":["관계된", "연루된"]}
for item in EngDic.keys():
    print(item, ":")
    for val in EngDic[item]:
        print(val, end="")
    print()

#디폴트인수
def sum_range(begin, end, step=1):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

print("sum = ", sum_range(1, 10))


#키워드인수
print("sum = ", sum_range(end = 10, begin = 1, step = 2))


#모듈과 이름 공간
from math import pow,sqrt #math 모듈에서 pow, sqrt 식별자를 이용
result = pow(2, 10)
dist = sqrt(1000)
print(result, dist)

#클래스
class Car:
    def __init__(self, color, speed = 0): #생성자 함수
        self.color = color
        self.speed = speed

    def speedUp(self): self.speed += 10 #가속 동작 : 속도 10 증가
    def speedDown(self): self.speed -= 10  # 감속 동작 : 속도 10 감소


car1 = Car('black', 0) # 1번째 자동차 까만색
car2 = Car('red', 120) # 2번째 자동차 빨간색 속도 120
car3 = Car('yellow', 40) # 3번째 자동차 노란색 속도 40
car4 = Car('blue', 0) # 4번째 자동차 파란색
car5 = Car('green') # 5번째 자동차 초록색

car2.speedDown() # car2 감속 : 속도 10 감소
car4.speedUp() # car4 가속 : 속도 10 증가

print(car2.speed)
car3.color = 'purple'
print(car3.color)

#클래스 상속
class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True):
        super().__init__(color, speed) # 부모(Car)클래스의 생성자 호출
        self.bTurbo = bTurbo # 터보모드를 위한 변수 생성 및 초기화

    def setTurbo(self, bTurbo = True): # 터보모드를 On/Off하는 메소드
        self.bTurbo = bTurbo

    def speedUp(self): # SuperCar의 SpeedUp. 메소드 재정의
        if self.bTurbo: # 터보 모드일때
            self.speed += 50 # 속도 업은 50씩
        else: # 아니면
            super().speedUp() # 기본 자동차 모드대로

    def __str__(self):
        if self.bTurbo:
            return "[%s][speed = %d] 터보모드" % (self.color, self.speed)
        else:
            return "[%s][speed = %d] 일반모드" % (self.color, self.speed)


#클래스 실습
class Employ:
    def __init__(self, name, career):
        self.name = name
        self.career = career

    def salary(self):
        if self.career <= 5:
            self.salary = (self.careeer * 100) + 3000
        elif self.career <= 10:
            self.salary = (self.career * 110) + 3500
        elif self.career > 10:
            self.salary = (self.career * 130) + 4000
        print("%s님의 연봉은 %d만원 입니다."%(self.name, self.salary))

    def degree(self):
        self.salary_d = int(self.salary) + 1000
        print("%s님의 연봉은 학위 소지로 인하여 %d만원 입니다."%(self.name, self.salary_d))

    def __getattr__(self, anything):
        print("잘못된 값입니다.")