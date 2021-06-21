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
print("소수 판별 프로그램")
list=[]
while True:
	n=int(input("20이상의 수를 입력하세요. [ Exit : 0 ]"))
	if n>=20:
		for i in range(1,n+1):
			for j in range(1,n+1):
				if i%j==0:
					list.append(i)
			if len(list)>2:
				print(i," 소수X")
			elif len(list)==2:
				print(i,"소수O")
			elif len(list)==1:
				print(i,"소수X")
			list=[]
	elif 1<=n<20:
		print("숫자가 틀렸습니다.")
	elif n==0:
		break


'''

2
1 2
0 0 소수O
3
1 2 3
0 1 0 소수O
4
1 2 3 4
0 0 1 0 소수X
5
1 2 3 4 5
0 1 2 1 0 소수O				
'''

	