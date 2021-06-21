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


print("<홍익대학교 과일 판매 머신>")
print("	1. orange : 1000원")
print("	2. strawberry : 2500원")
print("	3. peach : 1500원")
print("	4. mange : 2000원")
print("	5. grape : 2000원")
print("	6.종료")

while True:
	no=input('구매 번호를 입력 하세요(1~6)')
	if no=="1":
		print("orange 1000원 입니다.")
	elif no=="2":
		print("strawberry 2500원 입니다.")
	elif no=="3":
		print("peach 1500원 입니다.")
	elif no=="4":
		print("mango 2000원 입니다.")
	elif no=="5":
		print("grape 2000원 입니다.")
	elif no=="6":
		break
	