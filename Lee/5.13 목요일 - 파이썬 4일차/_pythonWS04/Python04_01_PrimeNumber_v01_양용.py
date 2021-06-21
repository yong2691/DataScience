'''
소수 판별 프로그램 작성

소수 요약 :
	1과 자기 자신만으로 나누어 떨어지는 1보다 큰 양의정수,
	이를테면 2,3,5,7,11,13,17,19,23,29,31...
	등 모두 소수 이다.

---------------------
파일명] Python04_01_PrimeNumber_양용

조건]
01. 사용자로 부터 20이상의 수를 입력 받는다.
- 이하인경우 : "숫자 확인하세요."
- 이상인경우 : 소수 판별 출력 한다.

Sample Run]
>> 20이상의 수를 입력하세요 [Exit:0] : 15
20이상의 숫자 입력하세요.

>> 20이상의 수를 입력 하세요 [Exit:0] : 20
1 소수 X
2 소수 O
3 소수 O
...
16 소수 x
17 소수 o
18 소수 x
...
'''

count=[]
while True:
	n=int(input("20이상의 수를 입력하세요. [ Exit : 0 ] : "))
	if n>=20 :
		for i in range(1,n+1):
			for j in range(1,i+1):
				if i%j==0:
					count.append(j)
				else:
					continue
			if len(count)==2:
				print(i,"은 소수O")
			else:
				print(i,"은 소수X")
			count=[]
	elif n==0:
		print("종료합니다.")
		break
	elif n<20:
		print("20 이상의 수를 다시 입력 하세요. [ Exit : 0 ] : ")


	