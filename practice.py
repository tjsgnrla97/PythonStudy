# 1. 숫자형

# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*3)
# print(3*(4+1))

# 2. 문자형

# print('풍선')
# print("나비")
# print("ㅋ"*9)

# 3. 논리형

# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not (5>10))

# 애완동물을 소개해 주세요~

# animal = "강아지"
# name = "유카리"
# age=7
# hobby="밥먹기"
# is_adult = age >= 3

# print("우리집 "+animal+"의 이름은 "+name+"입니다")
# hobby="공놀이"
# print(name+"는 "+str(age)+"살이며, 살이 많이 쪘습니다 "+hobby+"를 아주 좋아합니다")
# print(name, "는 어른일까요? ", is_adult)

# Quiz 1) 변수를 이용하여 다음 문장을 출력하시오

# 변수명 : station

# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력

# 출력 문장 : XX 행 열차가 들어오고 있습니다

# station = "사당"
# print(station+" 행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station+" 행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station+" 행 열차가 들어오고 있습니다.")

# 4. 연산자

# print(1+1) #2
# print(3-2) #1
# print(6*2) #12
# print(2/2) #1.0

# print(2**3) #8
# print(5%3) #2
# print(10%3) #1
# print(5//3) #1
# print(10/4) #2.5
# print(10//4) #2

# print(10>3) #True
# print(4>=7) #False
# print(5<=5) #True

# print(3==3) #True
# print(4==2) #False
# print(3+4==7) #True

# print(1 != 3) #True
# print(not(1 != 3)) #False

# print((3>0) and (3<5)) #True
# print((3>0) & (3<5)) #True

# print((3>0) or (3>5)) #True
# print((3>0) | (3>5)) #True

# print(5>4>3) #True
# print(5>4>7) #False

# 5. 수식

# print(2+3*4) #14
# print((2+3)*4) #20
# number = 2+3*4 #14
# print(number)
# number += 2 # 16
# print(number)
# number *= 2 # 32
# print(number)
# number -= 2 #30
# print(number)
# number /= 2 #15.0
# print(number)

# number %= 5 #0.0
# print(number)

# 6. 숫자 처리 함수

# print(abs(-5)) # 5
# print(pow(4,3)) # 64
# print(max(5,12)) # 12
# print(min(3,12)) # 3
# print(round(3.14)) #3 반올림
# print(round(4.64)) #5

# from math import *
# print(floor(4.99)) #4 내림
# print(ceil(3.14)) #4 올림
# print(sqrt(16)) #4.0 제곱근

# 7. 랜덤 함수(난수)

# from random import *

# print(random()) #난수 0.0~1.0 미만의 임의의 값 생성
# print(random() * 10) #0.0~10.0 미만의 임의의 값 생성
# print(int(random()*10)) #0.0~10.0 미만의 임의의 정수값 생성
# print(int(random()*10)) #0.0~10.0 미만의 임의의 정수값 생성
# print(int(random()*10)) #0.0~10.0 미만의 임의의 정수값 생성
# print(int(random()*10)+1) #1 ~ 11 미만의 임의의 정수 생성 
# print(int(random()*10)+1) #1 ~ 11 미만의 임의의 정수 생성 
# print(int(random()*10)+1) #1 ~ 11 미만의 임의의 정수 생성 
# print(int(random()*10)+1) #1 ~ 11 미만의 임의의 정수 생성 

# print(int(random()*45)+1) #1~45 이하의 임의의 정수값 생성
# print(int(random()*45)+1) #1~45 이하의 임의의 정수값 생성
# print(int(random()*45)+1) #1~45 이하의 임의의 정수값 생성
# print(int(random()*45)+1) #1~45 이하의 임의의 정수값 생성

# print(randrange(1,45)) #1~45 미만의 임의의 정수 값 생성
# print(randrange(1,46)) #1~45 이하의 임의의 정수 값 생성
# print(randint(1,45)) #1~45 이하의 임의의 정수값 생성

# Quiz 2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

# from random import *

# print("오프라인 스터디 모임 날짜는 매월 "+str(randint(4,28))+" 일로 선정되었습니다.")

# 8. 문자열

# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# 9. 슬라이싱

# jumin = "970127-1234567"
# print("성별 : "+jumin[7])
# print("연 : "+jumin[0:2]) #0번 인덱스부터 2번 인덱스 직전까지 (0,1)
# print("월 : "+jumin[2:4])
# print("일 : "+jumin[4:6])
# print("생년월일 : "+jumin[:6]) #처음 인덱스부터 6인덱스 직전까지
# print("뒷자리 7자리 : "+jumin[7:]) #7번 인덱스부터 끝까지
# print("뒷자리 7자리 (뒤에부터) : "+ jumin[-7:]) #맨 뒤에서 7번째 인덱스부터 끝까지

# 10. 문자열 처리 함수

# python = "Python is Amazing"

# print(python.lower()) #소문자
# print(python.upper()) #대문자
# print(python[0].isupper()) #True
# print(python[0].islower()) #False
# print(len(python)) #python 문자열 길이
# print(python.replace("Python","Java")) #특정 문자열 변환

# indexNum = python.index("n") #해당 문자열에서 특정 문자열이 몇번째 인덱스부터 존재하는지
# print(indexNum)
# indexNum = python.index("n",indexNum+1) #첫번째 찾은 인덱스 다음부터 탐색 
# print(indexNum)

# print(python.find("Java")) #탐색 문자열이 없으면 -1 반환
# print(python.index("Java")) #탐색 문자열이 없으면 Value Error와 함께 프로그램 종료
# print("hi")

# print(python.count("n")) #해당 문자열에서 특정 문자열이 총 몇번 포함되는지

# 11. 문자열 포맷

# print("a"+"b") ab
# print("a","b") a b

# 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")

# %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아합니다." % ("파란","빨간"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간")) #포맷인덱스 지정
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간")) #포맷인덱스 지정

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20,color="빨간"))

# 방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 12. 탈출문자

# \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내 따옴표 사용
# 저는 "울리시아"입니다.
# print('저는 "울리시아"입니다.')
# print("저는 \"울리시아\"입니다.")

#\\ : 문장 내 \ 사용
# print("D:\\GitHub\\PythonStudy")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t  : 탭
# print("Red\tApple")

# Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리(nav)+글자갯수(5)+글자내'e'갯수(1)+"!"(!)로 구성
                                                   
# 예) 생성된 비밀번호 : nav51!

# url="http://naver.com"
# output=url.replace("http://","") #규칙1
# output=output[:output.index(".")] #규칙2
# output=output[:3]+str(len(output))+str(output.count("e"))+"!" #규칙3
# print(f"{url}의 비밀번호는 {output}입니다.")

# 13. 리스트

# [] 순서를 가지는 객체의 집합

#지하철 칸 별로 10명, 20명, 30명
# subway1=10
# subway2=20
# subway3=30

# subway=[10,20,30]
# print(subway)

# subway=["울리시아","벨로그","티스토리"]
# print(subway)

# #울리시아가 몇 번째 칸에 타고 있는가?
# print(subway.index("울리시아"))

# #네이버가 다음 정류장에서 다음 칸에 탐
# subway.append("네이버")
# print(subway)

# #카카오가 울리시아와 벨로그 사이에 탐
# subway.insert(1,"카카오")
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
# # print(subway.pop())
# # print(subway)
# # print(subway.pop())
# # print(subway)

# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append("울리시아")
# print(subway)
# print(subway.count("울리시아"))

# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["울리시아",20,True]
# # print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 14. 사전(딕셔너리)
# key, value
# key 중복 안됨
# 사전명 = {key:value}
# cabinet = {3:"울리시아",100:"벨로그"}
# print(cabinet)
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(100))

# # print(cabinet[5]) #KeyError : 5 프로그램종료
# print(cabinet.get(5)) #None 프로그램 계속
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3":"울리시아", "B-100":"벨로그"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "네이버"
# cabinet["C-20"] = "티스토리"
# print(cabinet)

# # 떠난 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# 15. 튜플
# 리스트와는 달리 내용 변경이나 추가 불가
# 리스트보다 속도가 빠름
# 변경되지 않는 종목에 사용
# menu = ("돈까스","치즈까스")
# print(menu)
# print(menu[0])
# print(menu[1])

# name = "울리시아"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

# (name, age, hobby) = ("울리시아", 20, "코딩")
# print(name,age,hobby)

# 16. 집합(set,세트)
# 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"울리시아","벨로그","티스토리"}
# python = set(["울리시아","네이버"])

# #교집합 (java 와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합
# print(java | python)
# print(java.union(python))

# # 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python을 할 줄 아는 사람이 늘어남
# python.add("벨로그")
# print(python)

# # java를 까먹음
# java.remove("벨로그")
# print(java)

# 17. 자료구조의 변경

#커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# Quiz 4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

# from random import *
# users = range(1,21) # 1부터 20까지 숫자 생성
# # print(type(users))
# users = list(users)
# # print(type(users))
# print(users)
# shuffle(users)
# print(users)

# winners = sample(users,4) # 4명 중 한명은 치킨, 3명은 커피

# print(" -- 당첨자 발표 -- ")
# print(f"치킨 당첨자 : {winners[0]}")
# print(f"커피 당첨자 : {winners[1:]}")
# print(" -- 축하합니다 -- ")

# 18. if(분기)
# weather = "rain"
# if 조건:
#     실행 명령문
# weather = input("오늘 날씨는 어때요? : ")
# if weather == "rain" or weather == "snow":
#     print("우산을 챙기세요.")
# elif weather == "dusk":
#     print("마스크를 챙기세요.")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? : "))
# if temp>=30:
#     print("너무 더워요. 나가지 마세요.")
# elif temp>=10 and temp<30:
#     print("괜찮은 날씨에요.")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요.")
# else:
#     print("너무 추워요. 나가지 마세요.")

# 18. for(반복문)
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for i in [1,2,3,4,5]:
#     print(f"대기번호 : {i}")

# for i in range(5): #0,1,2,3,4
#     print(f"대기번호 : {i}")
# for i in range(1,6): #1,2,3,4,5
#     print(f"대기번호 : {i}")

# starbucks = ["울리시아","벨로그","티스토리"]
# for customer in starbucks:
#     print(f"{customer}, 커피가 준비되었습니다.")

# 19. while(반복문)
