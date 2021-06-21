'''
다른 주소를 가리키도록 만들수는 없을까?
'''

a=[1,2,3]
b=a[:]
a[1]=4
print(a)
print(b)

from copy import copy #외부 모듈을 가져올 때 import 사용.
a=[1,2,3]
b=copy(a) #이렇게 copy를 하면 다른 객체가 생성되는것이다.
print(b)
print(id(a)) #a와 b는 서로 다른 객체이므로, 경로는 달라진다.
print(id(b))
print(a is b)