
'''
첫 숫자와 다른 숫자들을 모두 비교해서 첫 숫자보다 작으면 교환
두번째 숫자와 다른 숫자들을 모두 비교해서 첫 숫자보다 작으면 교환
'''

list=[2,5,6,1,2,8,33,77,12]

for i in range(len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			list.insert(i,list[j])
			del list[j+1]
print(list)

'''
outer
	- idx : 0, len : -1

inner
	- idx : 1, len
'''