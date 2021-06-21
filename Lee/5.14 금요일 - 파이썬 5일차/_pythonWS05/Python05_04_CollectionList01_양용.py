# list는 []로 표시한다.

a=[]
b=[1,2,3]
c=['Life','is','too','short']
d=[1,2,'Life','is']
e=[1,2,['Life','is']] #list 안에 list 타입으로 들어가있다.
print(e[2])
print(e[-1][0],e[-1][1])

f=[1,2,['A','B',['C','D']]]
print(f[2][2][0])

#비어있는 리스트는 a=list() 로 생성할수도있다.

#리스트의 인덱싱과 슬라이싱
a=[1,2,3]
print(a[0])
print(a[0]+a[2])
print(a[-1])
print("*"*15,end="\n\n")
