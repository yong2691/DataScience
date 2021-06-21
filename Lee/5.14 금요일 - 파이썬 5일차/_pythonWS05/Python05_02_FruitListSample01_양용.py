'''
Algorithm 확인

조건]
	01. 10 이상의 숫자를 입력 받는다.
	02. 10 이하의 숫자이면,
	^ 10 이상의 숫자를 확인 하세요.
	03. 10이상이라면,
		- 3으로 나눠 떨어진 수 : Apple
		- 4으로 나눠 떨어진 수 : Melon
		- 5으로 나눠 떨어진 수 : Grape
		- 8으로 나눠 떨어진 수 : StrawBerry

Sampel Run ]
	>> 10 이상의 수를 입력 하세요 [ Exit : 0 ] : 9
	^ 10 이상의 숫자 확인 하세요.
	>> 10 이상의 수를 입력 하세요. [ Exit : 0 ] :15
'''

list=[]
cnt=[]

while True:
	n=int(input("10 이상의 수를 입력하세요 [ Exit : 0 ] : "))
	if n==0:
		print("종료합니다.")
		break
	elif n<10:
		print("10 이상의 수를 다시 입력하세요.")
	elif n>=10:
		for n in range(1,n+1):
			if n%3==0:
				list.append("Apple")
			if n%4==0:
				list.append("Melons")
			if n%5==0:
				list.append("Grape")
			if n%8==0:
				list.append("StrawBerry")
			cnt=cnt+list
			if len(list)==0:
				print("%d." %n)
			else:
				print("%d" %n,list)
			list=[]

		print(end="\n\n")
		print("="*30)
		print(end="\n\n")

		print("연산이 완료 되었습니다.",end="\n\n")

		print("Apple은 %d회 출력 되었습니다." %cnt.count('Apple'))
		print("Apple은 %d회 출력 되었습니다." %cnt.count('Melons'))
		print("Apple은 %d회 출력 되었습니다." %cnt.count('Grape'))
		print("Apple은 %d회 출력 되었습니다." %cnt.count('StrawBerry'))