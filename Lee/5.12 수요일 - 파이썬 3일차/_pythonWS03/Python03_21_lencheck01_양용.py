score=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

print("학생수 : ",len(score),"명") #리스트 안에 몇개가 들어있는지 파악
sum=0
for jumsu in score:
	sum=sum+jumsu

print("합계 : ", sum,"점")
print("평균 : ", "%0.2f" % int(sum/len(score)),"점")












a = "Life is too short, you need python"

if "wife" in a:
	print("wife")
elif "python" in a and "you" not in a:
	print("python")
elif "shirt" not in a:
	print("shirt")
elif "need" in a:
	print("need")
else:
	print("none")


for i in range(5,0,-1):
	for j in range(0,i):
		print("*",end="")
	print('')

for i in range(1,1000,3):
	sum=0
	sum=sum+i
	print(sum,end="")