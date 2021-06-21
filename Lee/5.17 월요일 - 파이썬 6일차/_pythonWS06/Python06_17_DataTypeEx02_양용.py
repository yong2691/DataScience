vI01=10
vI02=20
print(id(vI01))
print(id(vI02))
print("-"*50)


vI01=10
vI02=10
print(id(vI01)) #이거랑 아래거랑 경로가 같다. 왜? 같은수니까
print(id(vI02))

a=[1,2,3]
b=a
print(id(a)) #a나 b나 경로가 같다. 왜? 같은 [1,2,3]이라는 리스트니까
print(id(b))







print(a is b)

a[1]=7 #리스트 index1번째 값을 7로 바꿔라
print(a)
