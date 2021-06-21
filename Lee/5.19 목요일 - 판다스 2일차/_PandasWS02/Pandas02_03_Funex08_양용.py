'''
전역변수 : 함수 외에 선언 = 모든 함수 공유
지역변수 : 함수 내에 선언 = 함수와 생명력을 같이 한다.

'''

# 함수 안에서 함수 밖의 변수를 변경하는 방법

a=1 # 전역변수
def vartest(a): #매개변수도 지역변수이다.
	a=a+2
	print(a) 

vartest(a) #지역 변수 ->결과값인 3
print(a)   #전역 변수 그냥 그대로 결과값1

'''
def vartest(b):
	b=b+1

vartest(3)
print(b) #에러. 왜냐면 b라는 변수는 함수 안에만 존재하는 것
#b라는 함수는 함수 안에서만 사용될 뿐이다.
'''
a=1
def vartest(a):
	a=a+1
	return a #호출 한 곳으로 

print(vartest(a))