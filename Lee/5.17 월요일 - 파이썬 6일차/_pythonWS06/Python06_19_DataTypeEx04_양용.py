a=[1,2,3] #1,2,3은 객체
b=a
print("a,b 변경전")
print(a)
print(b)#프린트 된 결과값은 값 이라고 부른다.

a[1]=4
print("a 리스트안에 2번째 index를 2->1로 변경 한 후")
print(a)
print(b) # a만 바꿨는데 b도 바뀐이유는? 2번라인에 b를 a와 같다는 변수로 놓았으니까
