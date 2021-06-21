a=['a','c','b']
a.reverse()
print(a)
print("-"*15)

#위치 반환(index)
a=['a','c','b']
print(a.index('b'))
print("-"*15)

a=[1,2,3]
a.insert(0,4)
print(a)

a.insert(1,5)
print(a)
#find는 없는 숫자를 찾게되면 -1 이 뜬다.
# 하지만 index는 없는 숫자 넣으면 에러 뜬다.
#insert는 (자리,숫자) 입력하면 숫자를 자리에 넣고 기존 숫자는 뒤로 미룬다