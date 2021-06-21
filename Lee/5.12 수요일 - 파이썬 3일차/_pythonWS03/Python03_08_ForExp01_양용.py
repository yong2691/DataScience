'''
a = [1,2,3,4] #리스트
result = []  #대괄호는 콜렉션 타입
for num in a:
	result.append(num*3)
print(result)

#변수는 a,result,num 3개이다.
#결과 [3, 6, 9, 12]

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

#결과 [3, 6, 9, 12]
'''
a=[1,2,3,4]
result=[num*3 for num in a if num%2==0]
print(result)

'''
for num in a:
	if num%2==0:
	print(num*3)
'''

