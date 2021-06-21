menu=['사과','딸기','참외']
money=[1000,2000,3000]

for n in range(0,3):
	print(n+1,"번",menu[n],":",money[n],"원")

while True:
	n=input("구매번호 입력해라 : ")
	n=int(n)
	if n==1:
		print(menu[n-1],"는",money[n-1],"원 입니다.")
	elif n==2:
		print(menu[n-1],"는",money[n-1],"원 입니다.")
	elif n==3:
		print(menu[n-1],"는",money[n-1],"원 입니다.")
	else:
		break
