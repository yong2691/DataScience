#연습문제1번
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



#연습문제2번

sum=0
for i in range(0,1000,3):
	sum=sum+i
print(sum)



#연습문제3번

for i in range(5,0,-1):
	for j in range(0,i):
		print("*",end="")
	print('')



#연습문제4번


for i in range(1,100):
	print(i)

#연습문제5번

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum=0
for jumsu in score:
	sum=sum+jumsu
print("합계:",sum)
print("평균:","%0.2f" %(sum/len(score)))  # 괄호 조심!!!


#연습문제6번

a=[1,2,3,4,5]
result=[num*2 for num in a if num%2==1]
print(result)

#위나 아래나 같은 결과값을 내놓는다.
#위는 리스트 내포 (list comprehension)
a=[1,2,3,4,5]
result=[]

for n in a:
	if n%2==1:
		result.append(n*2)
print(result)

