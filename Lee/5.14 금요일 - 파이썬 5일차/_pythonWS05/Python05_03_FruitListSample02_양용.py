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


list=["Apple","Melon","Grape","StrawBerry"]
num=[3,4,5,8]
cnt=[0,0,0,0]

while True:
	n=int(input("10 이상의 수를 입력하세요 [exit=0] : "))
	if n==0:
		print("종료합니다.")
		break
	if n<10:
		print("10 이상의 수를 다시 입력하세요.")
	elif n>=10:
		print("== %d 회 반복합니다." %n)
		for i in range(1,n+1):
			print("\n%2d." %i,end="")
			for j in range(len(list)):
				if (i%num[j]==0):
					cnt[j]=cnt[j]+1
					print("%s" %list[j],end=" ")
	print("\n\n==<<Fruit Count List>>==\n\n")
	for i in range(len(list)):
		print("%d. %-12s %2d회" % (i+1, list[i], cnt[i]))
	cnt=[0,0,0,0]
