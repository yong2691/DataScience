'''
***********홍대 과일 판매 머신 V10***********
	1. orange : 1000원
	2. strawberry : 2500원
	3. peach : 1500원
	4. mange : 2000원
	5. grape : 2000원
	6. 종료

구매 번호를 입력 하세요(1~5):
조건01 : 해당 번호를 입력하면, Orange 1000원 입니다. 문구
조건02 : 
automachine_Step01_양용
'''
menu=['오렌지','딸기','복숭아','망고','포도','종료']

print("<홍익대학교 과일 판매 머신 ver.02>")

for num in range(0,6):
	print(num+1,"번",menu[num])

while True:
	num=input('구매 번호를 입력 하세요(1~6)')
	if int(num)==0:
		print("orange 1000원 입니다.")
	elif num=="1":
		print("strawberry 2500원 입니다.")
	elif num=="2":
		print("peach 1500원 입니다.")
	elif num=="3":
		print("mango 2000원 입니다.")
	elif num=="4":
		print("grape 2000원 입니다.")
	elif num=="5":
		break
	