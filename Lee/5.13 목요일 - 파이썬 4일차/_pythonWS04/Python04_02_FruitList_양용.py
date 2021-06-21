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
a=0
m=0
g=0
s=0

result=[]
while True:
		n=int(input("10 이상의 숫자를 입력하세요. [Exit:0] : "))
		print("=====",n,"번 반복합니다.","=====")
		if n==0:
			print("종료합니다.",end="\n\n")
			break
		elif n<10:
			print("10 이상의 수가 아닙니다.")
		elif n>=10:
			for n in range(1,n+1):
				if n%3==0:
					result.append("apple")
					a=a+1
				if n%4==0:
					result.append("Melons")
					m=m+1
				if n%5==0:
					result.append("Grape")
					g=g+1
				if n%8==0:
					result.append("StrawBerry")
					s=s+1
				if len(result)>0:
					print("%d. %s" %(n,result))
				if len(result)==0:
					print("%d." %n)
				result=[]

		print(end="\n\n")
		print(" == << Fruit Count List >> ==",end="\n\n")
		print("apple은 %d입니다." %a,end="\n\n")
		print("melons는 %d입니다." %m,end="\n\n")
		print("grape는 %d입니다." %g,end="\n\n")
		print("strawberry는 %d입니다." %s,end="\n\n")

#누적연산자는 변수=변수+1 이렇게 해도 된다.
#또는 어펜드를 사용해도 가능
