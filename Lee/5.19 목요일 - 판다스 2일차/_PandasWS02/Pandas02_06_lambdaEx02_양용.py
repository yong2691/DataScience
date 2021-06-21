#lambda 활용법

x = lambda a : a+10
print(x(5))

x=lambda a,b:a*b
print(x(5,6))

def myfunc(n):
	return lambda a: a*n

mydoubler=myfunc(2) # lambda a : a*n을 받아서 n에 2를 넣엇고
print(mydoubler(11)) # a에다가 11을 넣엇은이까 출력할 결과는 11*2이다.

#람다에 넣은값에 3배 하고 싶을 때,
def myfunc(n):
	return lambda a:a*n

mytripler=myfunc(3)
print(mytripler(11))