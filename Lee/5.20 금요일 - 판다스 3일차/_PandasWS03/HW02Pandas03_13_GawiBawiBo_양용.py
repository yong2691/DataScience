'''
	1.가위	2.바위	3.보	4.횟수입력	9.종료
	번호를 선택하세요. 2
	Com : 가위 / User : 바위			You win! 당신이 이겼습니다!
	=>	현재 스코어 5 :6 (컴퓨터 : 당신) 입니다.

-----------------------------------------------------------------------

	1. 가위	2. 바위	3. 보	4. 횟수입력 9.종료
	번호를 선택하세요. 9
	총 14회의 게임 중 컴퓨터가 5회, 당신이 6회 이겼습니다.
	따라서 최종 스코어 5 : 6 (컴퓨터 : 당신)로 당신의 승리입니다.

'''

import random
print("%-10s" %"1.가위","%-10s"%"2.바위","%-10s"%"3.보", "%-10s" %"4.횟수입력","%-10s" %"9.종료")

GBB = ['가위','바위','보']
result = []
win = []
loose = []
while True:
	'''여기에다가 넣으면, 계속해서 초기화 되니까 while True 바깥에다가 넣어야 한다.
	result = []
	win = []
	loose = [] 
	'''
	n=int(input("번호를 선택하세요."))
	m=int(random.randint(1,3))
	if n == 4 :
		print('총 %s회의 게임에서 컴퓨터가 %s회 당신이 %s회 이겼습니다.' %(len(result),len(loose),len(win)))
	elif n == 9 :
		print('총 %s회의 게임 중, 컴퓨터가 %s회, 당신이 %s회 이겼습니다.' %(len(result),len(loose),len(win)) )
		if len(win) > len(loose) :
			print('따라서 최종 스코어 %s : %s (컴퓨터 : 당신)로 당신의 승리입니다.' %(len(loose),len(win)))
		if len(win) < len(loose) :
			print('따라서 최종 스코어 %s : %s (컴퓨터 : 당신)로 컴퓨터의 승리입니다.' %(len(loose),len(win)))
		if len(win) == len(loose) :
			print('따라서 최종 스코어 %s : %s (컴퓨터 : 당신)로 무승부 입니다.' %(len(loose),len(win)))
		break


	elif n >3 :
		print('\t','잘못 입력되었습니다. 1~3의 수를 입력하세요.')
	elif n == m :
		print('\t',"Com : %s / User : %s       무승부! 비겼습니다!" %(GBB[n-1], GBB[m-1]))
		result.append(n)


	elif n == 1 and m == 3:
		print('\t',"Com : %s / User : %s       당신이 이겼습니다." %(GBB[n-1], GBB[m-1]))
		result.append(n)
		win.append(n)
	elif n-1 == m :
		print('\t',"Com : %s / User : %s       당신이 이겼습니다." %(GBB[n-1], GBB[m-1]))
		result.append(n)
		win.append(n)


	elif n+1 == m :
		print('\t',"Com : %s / User : %s       당신이 졌습니다." %(GBB[n-1], GBB[m-1]))
		result.append(n)
		loose.append(n)
	elif n == 3 and m == 1:
		print('\t',"Com : %s / User : %s       당신이 이겼습니다." %(GBB[n-1], GBB[m-1]))
		result.append(n)
		loose.append(n)
	print('=> 현재 Score Com : %s vs User : %s 입니다.' %(len(loose),len(win)))


	if len(win) > len(loose):
		print('\t','당신이 이기고 있습니다.')
	if len(win) < len(loose):
		print('\t','당신이 지고 있습니다. 분발하세요.')
	if len(win) == len(loose):
		print('\t','비기고 있습니다..')
