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
money=[1000,2500,1500,2000,2000]

#위에건 리스트 자료형 
#리스트는 0부터 시작 - 0번,1번,2번,3번,4번,5번 이렇게 읽는다.

print("<홍익대학교 과일 판매 머신 ver.03>")

# 위에 제목을 쓰고

for num in range(0,5):
	print(num+1,"번",menu[num],":",money[num],"원")
print("6.종료")

# 위에 메뉴판을 보여주고
# 이제 선택하면 된다.

while True:
	n=input('구매 번호를 입력 하세요(1~6)') #입력할 번호
	n=int(n) # intager니까 입력은 숫자로 받아 들일 것이다.
	if n==1:
		print(menu[n-1],"는",money[n-1],"원입니다.")
	elif n==2:
		print(menu[n-1],"는",money[n-1],"원입니다.")
	elif n==3:
		print(menu[n-1],"는",money[n-1],"원입니다.")
	elif n==4:
		print(menu[n-1],"는",money[n-1],"원입니다.")
	elif n==5:
		print(menu[n-1],"는",money[n-1],"원입니다.")
	elif n==6:
		break
	