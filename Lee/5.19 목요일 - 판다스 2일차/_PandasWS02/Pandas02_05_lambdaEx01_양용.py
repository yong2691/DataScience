# lanbda
'''
lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
보통 함수를 한줄로 간결하게 만들때 사용한다.
우리말로는 "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나
def를 사용할 수 없는 곳에 주로 쓰인다.

사용형식]
lambda 매개변수1, 매개변수2 : 매개변수를 이용한 표현식

람다의 특징은 리턴이 없어도 무조건 반환해준다.


'''


add=lambda a,b:a+b #a+b를 add에다가 반환해준다.
result = add(3,4) #람다 add 함수를 result 변수에 저장
print(result)



def add(a,b):
	return a+b
print(add(3,4))