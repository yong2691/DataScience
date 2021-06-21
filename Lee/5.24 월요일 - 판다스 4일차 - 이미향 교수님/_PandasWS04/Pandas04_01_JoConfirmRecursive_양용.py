'''
input() 함수 이용
	결과 : 4인 이상의 이름을 입력하세요.(SB로 구분한다) : 보라돌이 나나
		- 4인이 아니면 ==> ^ 명수를 확인하세요 (4인이상)
		- 4인 이상이라면 ==> 보라돌이 나나 뚜비 뽀오 입력되었
'''
import random
list = []

def recursive (m) : #recursive는 재귀함수 이다.
	if (chk == len(list)):
		return
	
	for i in range(m):
		num = random.randint(1,len(name))
		if num not in list:
			list.append(num)
		else:
			recursive(chk-len(list)) #재귀함수

while True:
	name = input('4인 이상의 이름을 입력하세요. (Space Bar로 구분한다.)').split()
#split을 할때는 스페이스바를 띄어놓고하고, 스페이스바는 컴마, 처리가 된다.
	if len(name) >= 4:
		for i in name:
			print(i,end=' ')
		print('')

		chk = len(name)

		list = []
		cnt=0

		recursive(chk)
		print(list)
