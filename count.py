# List 사용하기 1
num = []
sum = 0
for i in range(5):
    newsum = int(input("%d번 숫자를 입력하십시오 : " %(i+1)))
    num.append(newsum)
for i in range(5):
    sum = sum + num[i]

print("숫자의 합계는",sum,"입니다")

# List 사용하기 2
number = []
for i in range(1,9,3): # 1부터 9까지 3씩 증가함
    small_list = [] #안에 들어가는 리스트
    for j in range(3): #123 반복
        small_list.append(i+j) # i + j 값 small_list에 추가
    number.append(small_list) #number list에 small_list 추가
print(number)


# List 사용하기 3
num = [] #리스트
count_plus = 0 #양의 정수의 개수
count_minus = 0 #음의 정수의 개수
for i in range(5): #1~5
    number = int(input("%d. 숫자입력 "%(i+1))) #숫자 넣어주기
    num.append(number) #리스트에 추가
for i in range(5): #1~5
    if num[i] > 0: #만약에 i번째 수가 0보다 크면
        count_plus+=1  #양의 정수의 개수 +1
    elif num[i] < 0: #0보다 작으면
        count_minus+=1 #음의 정수의 개수 +1
print(f"양의 정수는 {count_plus}개, 음의 정수는 {count_minus}개")