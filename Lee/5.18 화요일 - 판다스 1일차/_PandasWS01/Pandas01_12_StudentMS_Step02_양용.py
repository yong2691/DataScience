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

# 점수 딕셔너리 생성 함수 = inputData
def inputData():
	for j in range(len(idList)):
		dic[idList[j]]=scoreList[j]

# 점수 나열 함수 = PrintList
def PrintList():
		print(menu[n-1])
		for i in range(len(MenuList)):
			print(MenuList[i],end="\t")
		print()
		print("="*60)
		for i in range(len(dic)):
			print(idList[i],"\t",dic[idList[i]][0],"\t",dic[idList[i]][1],"\t",dic[idList[i]][2],"\t")


dic = {}
values=[]
deleteIDList = []
idx = 0;


inputData()
#아래 두줄을 inputData() 함수로 대체 한 것이다.
#왜냐면 위에서 inputData 함수를 def 했으니까!
#for i in range(len(idList)):
	#dic[idList[i]]= scoreList[i]

# 1번문제 :
# dic에 idList를 key값으로 하고, scoreList를 Value 값으로 할당
#딕셔너리 만들기. dic[key값]=value값

while True:
	n=int(input("%20s" %"메뉴의 번호를 선택하세요. "))
	if n==int(menuChk[n-5]):
		print("\n")
		print("%20s" %"종료합니다.")
		print("\n")
		break

	elif n==1:
		print("\n")
		print("%20s" %menu[n-1],"Algorithm Chk")
		print("\n")
	elif n==2:
		print("\n")
		print("%20s" %menu[n-1],"Algorithm Chk")
		print("\n")
	elif n==3:
		PrintList()
		print("\n")
	elif n==4:
		print("\n")
		print("%20s" %menu[n-1],"Algorithm Chk")
		print("\n")
