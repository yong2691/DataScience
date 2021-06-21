while True:
	n=int(input("10 이상의 수를 입력하세요 [ Exit : 0 ] : "))
	if n==0:
		print("종료합니다.")
		break
	elif n<10:
		print("10 이상의 수를 다시 입력하세요.")
	elif n>=10:
		print("10 이상의 수를 다시 입력하세요.")