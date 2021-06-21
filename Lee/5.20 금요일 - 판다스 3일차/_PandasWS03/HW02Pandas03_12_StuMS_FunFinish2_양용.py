'''
========================메뉴선택========================

1. 탈퇴학생 2. 추가등록 3. 학생목록  4. 합격생목록 9.메뉴종료

========================================================

메뉴의 번호를 선택해주세요.
1. 탈퇴학생 (Algorithm Chk)
DelID()
	01. ID 없는 경우 : 해당 아이디 없음
	02. ID 있는 경우 : deleteIDList = [] (한번 탈퇴하면, 두번 가입할 수 없어)
	입력한 아이디에 대해서 idList.index(원하는ID가있는 idx번호) 를 찾아서 그 인덱스 위치에 존재하는 ID값을 삭제
	+ 그 인덱스 위치에 존재하는 scoreList에 해당하는 점수를 찾아서 score 값을 삭제
	03. 삭제
2. 추가등록 (Algorithm Chk)
SignIn()
	01. ID가 중복된 경우 : 중복 아이디 있음.
	02. ID 입력 받는다 << 기존 탈퇴 했다면, << "탈퇴회원 가입 불가"
	03. 탈퇴학생이 아니고 중복이 아닌 경우 : 4개 값 입력 받는다.
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

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

################################################# 여기서부터 함수 define

#def01. 점수 딕셔너리 생성 함수 = inputData
def inputData():
	for j in range(len(idList)):
		dic[idList[j]]=scoreList[j]



#def02. 점수 나열 함수 = PrintList
def PrintList():
	print("학생목록")
	for i in MenuList:
		print(i,end="\t")
	print()
	print("="*60)
	for i in dic.keys(): #여기서 포문 돌리는 게 idList로 돌리고 있어서 계속 오류가 났었다. 왜냐면 idList는 건들지 않았으니까, 업데이트가 되지 않았다.
		printData(i)
		DataSum(i)
		DataAvg(i)
		PassCHK(i)

#def03. 학생 목록 점수값들 

def printData(i):
	print(i,"\t",end=' ')
	print(dic[i][0],"\t",dic[i][1],"\t",dic[i][2],"\t",end=' ')

def DataSum(i):
	print(dic[i][0]+dic[i][1]+dic[i][2],"\t", end=' ')

def DataAvg(i):
	print("%d" %((dic[i][0]+dic[i][1]+dic[i][2])/3),"\t",end=' ')

def PassCHK(i):
	if ((dic[i][0]+dic[i][1]+dic[i][2])/3) >= 70 :
		print("합격")
	else:
		print("불합격")

#def04. DelID
def DelID():
	n=input("아이디를 입력하세요")
	if n not in dic.keys():
		print("존재하지 않는 아이디 입니다.")
	elif n in dic.keys():
		del dic[n]
		deleteIDList.append(n)

#def05. SignIn()
def SignIn():
	n=input("아이디를 입력하세요")
	if n in dic.keys():
		print("중복된 아이디 입니다.")
	elif n == str(deleteIDList[:]):
		print("탈퇴 회원 가입 불가합니다.")
	else :
		b=int(input("필기 점수를 입력하세요."))
		c=int(input("실기 점수를 입력하세요."))
		d=int(input("인성 점수를 입력하세요."))
	dic[n] = [b,c,d]
	print(dic)

#def06. 메인 프로그램 함수 = Mainpg
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
		PrintList()
	elif n==4:
		PassIDList()

#def07. 합격생 목록
def PassIDList():
	for j in dic.keys():
		if ((dic[j][0]+dic[j][1]+dic[j][2])/3) >= 70:
			print(j,"는 합격입니다.")
		else:
			continue


######################################### 여기서부터 알고리즘

print("========================메뉴선택========================")
print("\n")
for i in range(0,len(menu)):
	print(menu[i],end="")
print("\n")
print("========================================================")
print("\n")

inputData()
while True: #while True를 Mainpg() 안에 넣어도 되지만, 그럼 함수 안에서 무한루프가 돌게 되니까 지금으로써는 함수 사용으로서의 의미가 없다.
	Mainpg()

