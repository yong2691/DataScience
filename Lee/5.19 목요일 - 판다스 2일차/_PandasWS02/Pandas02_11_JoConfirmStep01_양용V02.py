'''
input() 함수 이용
	결과 : 4인 이상의 이름을 입력하세요.(SB로 구분한다) : 보라돌이 나나
		- 4인이 아니면 ==> ^ 명수를 확인하세요 (4인이상)
		- 4인 이상이라면 ==> 보라돌이 나나 뚜비 뽀오 입력되었
'''


while True:
	n=[]
	n=input("4인 이상의 이름을 입력하세요.").split()
	if '0' in n:
		sys.exit()
	
	if len(n) < 4:
		print("^\t 명수를 확인하세요.")
		continue
	else:
		for i in n:
			print(i,end=' ')
		print("입력되었습니다.")
