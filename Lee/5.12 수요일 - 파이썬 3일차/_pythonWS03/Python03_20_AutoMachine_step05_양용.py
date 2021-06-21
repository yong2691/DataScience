
menu=['오렌지','딸기','복숭아','망고','포도','수박','수박바','종료']
money=[1000,2500,1500,2000,2000,13000,750]

#위에건 리스트 자료형 
#리스트는 0부터 시작 - 0번,1번,2번,3번,4번,5번 이렇게 읽는다.

print("<홍익대학교 과일 판매 머신 ver.03>")

for num in range(0,7):
	print("%s %s %s%30s" %(num+1,"번",menu[num],":"),money[num],"원")
print("8.종료")

while True:
	n=input('코인을 투입하세요.')
	n=int(n)
	print("투입된 금액은",n,"원 입니다.")
	m=input("구매 번호를 입력 하세요(1~6)")
	m=int(m)

	if m in range(1,8):
		print("선택한 과일은",menu[m-1],"입니다.")
		print("받은 금액은",n,"원 입니다.")
		if n>=money[m-1]:
			print("거스름돈은",n-money[m-1],"원 입니다. 안녕히가세요...")
			break
		elif n<money[m-1]:
			print("금액부족 확인하세요.")

	else:
		print("반환되는 금액",n,"원 확인하세요...")
		break
