'''
a=[1,2,3,4]
result=[num*3 for num in a if num%2==0]
print(result)


result=[x*y for x in range(2,10) for y in range(1,10)]
print(result)
'''


for i in range(1,6): #1~5까지 도는 것.
	for j in range(0,i):
# 첫번째돌때는 0~1 이고, 두번째 돌땐, 0~2 이고 ...다섯번째돌땐 0~5
		print("*",end="") #별을 반복해서 출력 ""는 바로옆에다가출력한다는뜻
	print('') # 이너포문 한번 돌고 한줄띄기




