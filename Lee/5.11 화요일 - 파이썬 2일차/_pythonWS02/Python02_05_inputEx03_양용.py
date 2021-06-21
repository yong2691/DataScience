''' <예제>
1. 실행시 2개의 갑을 입력.
2. vID, vPwd
3. id가 "Orange"이고, pwd가 "HappyDay" 이면,
"반갑습니다. 회원님" 아니면, "회원가입 확인 하세요."
'''

print("아이디를 입력하세요.")

vID=input()
if str(vID)== "Orange":
	print("비밀 번호를 입력하세요.")
else:
	print("회원가입 확인 하세요.")

vPwd=input()
if str(vPwd)=="1234":
	print("반갑습니다. 회원님")
else:
	print("회원가입 확인 하세요.")
