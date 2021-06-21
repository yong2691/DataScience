'''
input() 함수 이용
	결과 : 4인 이상의 이름을 입력하세요.(SB로 구분한다) : 보라돌이 나나
		- 4인이 아니면 ==> ^ 명수를 확인하세요 (4인이상)
		- 4인 이상이라면 ==> 보라돌이 나나 뚜비 뽀오 입력되었
'''
import random
while True:
	a=[]
	b=[]
	a=input("4인 이상의 이름을 입력하세요.").split()
	if '0' in a:
		sys.exit()
	
	if len(a) < 4:
		print("^\t 명수를 확인하세요.")
		continue
	else:
		while True:
			num=random.randint(1,len(a)) 
			if num not in b:
				b.append(num)
			else:
				continue
			if len(b)==len(a):
				break
	for i in a:
		print(i,end=' ')
	print('이고,')
	for i in b:
		print(i,end=' ')
	print("입니다.")

'''
4인 이상일 경우, len() 으로 인원수 반환 받고
5명이면, -> 1 ~ 5
중복 없이 반환
Sample Run ]
	보라돌이 뽀오 나나 뚜비
	   4            1       2      3 랜덤하게 번호를 받는다.

for idx in range(len(list[]):
	random값 반환
	for idx in range(5):
		앞쪽비교 idx-1
	list01=[4,4,_?
'''