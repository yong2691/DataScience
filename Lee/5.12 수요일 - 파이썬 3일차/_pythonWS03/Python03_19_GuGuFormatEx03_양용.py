#아래의 3가지 알고리즘 먼저 짜는게 60%이다.
#1. 행/열
#2. j * i = (i*j)
#3. format

for n in range(2,10): # 단일 포문
	print("# %d단" %n, end="  ")
print("\n\n")


print("="*55)

for i in range(2,10):
	for j in range(2,10):
		print("%dx%d=%-2d" %(j,i,i*j),end="  ")
#print(i,"x",j,"=","%-2d" %(i*j),end="  ")
#으로 해도 되는데 한칸씩 띄어진다.
#"%-1d"는 왼쪽정렬, 그리고  %(i*j) 에서 ()는 반드시 해야 한다.
	print ('')
	print ('')
print("="*55)


