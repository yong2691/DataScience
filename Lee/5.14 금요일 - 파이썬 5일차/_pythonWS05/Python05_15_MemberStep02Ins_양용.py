'''
========================메뉴선택========================

1. 회원가입 2. 로그인 3. 회원목록  9.메뉴종료

========================================================

메뉴의 번호를 선택해주세요.
1. 회원가입 (Algorithm Chk)
메뉴의 번호를 선택해주세요.
2. 로그인 (Algorithm Chk)
메뉴의 번호를 선택해주세요.
3. 회원목록 (Algorithm Chk)
메뉴의 번호를 선택해주세요.
'''

print("========================메뉴선택========================")
print("\n")
print("1. 회원가입 2. 로그인 3. 회원목록 9.메뉴종료")
print("\n")
print("========================================================")
print("\n")


menu=["1.회원가입","2.로그인","3.회원목록","9.종료"]
menuchk=['1','2','3','9']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
m=[]
while True:
	n=input("        메뉴의 번호를 선택해주세요. [ exit : 9 ] ")
	print("\n")
	if n=="":
		print("chk")
		print("\n")
	
	else:
		n=int(n)
		if n==1:
			print("%-10s" %"Sign Up")
			ID=input("%-10s : " %"ID")
			PWD=input("%-10s : " %"PWD")
			NAME=input("%-10s : " %"NAME")
			EMAIL=input("%-10s : " %"EMAIL")
			PHONE=input("%-10s : " %"PHONE")
			ADDRESS=input("%-10s : " %"ADDRESS")
			m.append([ID,PWD,NAME,EMAIL,PHONE,ADDRESS])
			print("          ","%-10s" %m,end="\n\n")
			print("          ","%-10s" %"현재 회원수는",len(m)," 명 입니다.")

		elif n==2:
			print("        ",menu[n-1],"Algorithm Chk")
		elif n==3:
			print("        ",menu[n-1],"Algorithm Chk")
		elif n==9:
			print("        ","종료.")
			print("\n")
			break
		else:
			print("        ","숫자를 다시 입력해 주세요.")
		print("\n")
