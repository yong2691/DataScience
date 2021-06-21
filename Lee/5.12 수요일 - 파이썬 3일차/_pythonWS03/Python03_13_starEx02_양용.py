
for i in range(5,0,-1): #step에 -1을 쓰면 1씩 내려오게된다. 그러니까 step에는 1이 default 값이다.
	for j in range(0,i):
		print("*",end="")
	print('')



print('')
'''
             outer i    inner j
*               1             1    
**             2            2
***           3            3
****         4            4
*****       5            5
'''
'''
                 행			열
             outer i    inner j
*****       1            5
****         2            4
***           3            3
**             4            2
*               5             1    
'''


for i in range(1,6):
	for j in range(0,6-i):
		print("*",end="")
	print('')

print('')
print('')
print('')

count=int(input("숫자를입력해라^^:"))

for i in range(count,0,-1): #3을 치면 3행,2행,1행 이 출력
	for j in range(i): #3열, 2열, 1열
		print ("*", end=" ")
	print()

