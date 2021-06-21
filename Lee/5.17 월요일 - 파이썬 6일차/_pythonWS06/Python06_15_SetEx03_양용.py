#집합 자료형 관련 함수들

#값 1개 추가하기(add)
s1=set([1,2,3])
s1.add(4)
print(s1)

#값 여러개 추가하기(update)
s1=set([1,2,3])
s1.update([4,5,6]) #4,5,6을s1 set에 뒤에다가 추가시킨다.
print(s1)

#특정 값 제거하기(remove)
s1=set([1,3,5])
s1.remove(3) #3에 해당하는 값을 지워준다.
print(s1)