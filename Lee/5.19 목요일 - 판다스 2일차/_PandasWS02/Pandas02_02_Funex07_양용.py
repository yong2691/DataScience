# 매개변수에 초깃값 미리 설정하기
# say_myself 함수는 3개의 매개변수를 받아서 마지막 인수인
# man이 True 이면 "남자입니다", False이면 "여자입니다"를 출력

def say_myself(name, old, man=True): #3번째 매개변수 default값 man
#3번째 매개변수값에다가 man=True 라는 의미는 3번째 값을 쓰지 않을 경우 default 값으로 남자가 출력된다.
	print("내 이름은 %s입니다." %name)
	print("내 나이는 %d살입니다." %old)

	if man:
		print("남자입니다.")
	else:
		print("여자입니다.")

say_myself("소나무",27)
say_myself("오렌지",25,False)