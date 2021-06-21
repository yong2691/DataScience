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

dic = {}
deleteIDList = []
idx = 0;

while True:
	n=int(input("%20s" %"메뉴의 번호를 선택하세요. "))
	if n==int(menuChk[n-5]):
		print("\n")
		print("%20s" %"종료합니다.")
		print("\n")
		break
	elif n==int(menuChk[n-1]):
		print("\n")
		print("%20s" %menu[n-1],"Algorithm Chk")
		print("\n")


