# return문을 2번 사용하면,
# 두 번째 return문인 return a*b는 실행되지 않았다

def add_and_mul(a,b):
	return a+b
	return a*b

# 이 리턴값은 어디로 가나? 자기를 호출해준 대로 간다.
#첫번째 리턴값이 적용되고, 두번째 리턴값은 실행되지 x
result = add_and_mul(2,3)
print(result)


#[return의 또 다른 쓰임새]
# return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다

def say_nick(nick):
	if nick=="바보":
		return
	print("나의 별명은 %s입니다." %nick)

say_nick('야호')
say_nick('바보')

