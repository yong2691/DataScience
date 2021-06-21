'''
========================메뉴선택========================

1. 탈퇴학생 2. 추가등록 3. 학생목록  4. 합격생목록 9.메뉴종료

========================================================

메뉴의 번호를 선택해주세요.
1. 탈퇴학생 (Algorithm Chk)
메뉴의 번호를 선택해주세요.
2. 추가등록 (Algorithm Chk)
메뉴의 번호를 선택해주세요.
3. 학생목록 (Algorithm Chk)
메뉴의 번호를 선택해주세요.
4. 합격생목록 (Algorithm Chk)
메뉴의 번호를 선택해주세요.
9. 메뉴종료

'''

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
newmenu=[]
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]
dic = {}
values=[]
deleteIDList = []
idx = 0;

print("========================메뉴선택========================")
print("\n")
for i in range(0,len(menu)):
	print(menu[i],end="")
print("\n")
print("========================================================")
print("\n")

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

#def01. 점수 딕셔너리 생성 함수 = inputData
def inputData():
	for j in range(len(idList)):
		dic[idList[j]]=scoreList[j]

#def02. 점수 나열 함수 = PrintList
def PrintList(n):
	print(menu[n-1])
	for i in range(len(MenuList)):
		print(MenuList[i],end="\t")
	print()
	print("="*60)
	for i in range(len(dic)):
		print(idList[i],"\t",dic[idList[i]][0],"\t",dic[idList[i]][1],"\t",dic[idList[i]][2],"\t")

#def03.
def DelID():
	return
#def04.
def SignIn():
	n=input("아이디를 입력하세요")
	if n in idList[:]:
		print("중복된 아이디 입니다.")
	elif n == Str(deleteIDList[:]):
		print("탈퇴 회원 가입 불가합니다.")
	else :
		a=input("ID를 입력하세요.")
		b=input("필기 점수를 입력하세요.")
		c=input("실기 점수를 입력하세요.")
		d=input("인성 점수를 입력하세요.")
		idList.append(a)
		scoreList.append(b,c,d)

#def05. 메인 프로그램 함수 = Mainpg
def Mainpg():
	n=int(input("%20s" %"메뉴의 번호를 선택하세요. "))
	if n==9:
		print("%20s" %"종료합니다.")
		exit()
	elif n==1:
		DelID()
	elif n==2:
		SignIn()
	elif n==3:
		PrintList(n)


inputData()
while True: #while True를 Mainpg() 안에 넣어도 되지만, 그럼 함수 안에서 무한루프가 돌게 되니까 지금으로써는 함수 사용으로서의 의미가 없다.
	Mainpg()

'''과제
DelID()
	01. ID 없는 경우 : 해당 아이디 없음
	02. ID 있는 경우 : deleteIDList = [] (한번 탈퇴하면, 두번 가입할 수 없어)
	입력한 아이디에 대해서 idList.index(원하는ID가있는 idx번호) 를 찾아서 그 인덱스 위치에 존재하는 ID값을 삭제
	+ 그 인덱스 위치에 존재하는 scoreList에 해당하는 점수를 찾아서 score 값을 삭제
	03. 삭제
SignIn()
	01. ID가 중복된 경우 : 중복 아이디 있음.
	02. ID 입력 받는다 << 기존 탈퇴 했다면, << "탈퇴회원 가입 불가"
	03. 탈퇴학생이 아니고 중복이 아닌 경우 : 4개 값 입력 받는다.
'''