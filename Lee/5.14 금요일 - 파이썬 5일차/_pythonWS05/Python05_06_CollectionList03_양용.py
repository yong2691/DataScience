# list는 []로 표시한다.


a=[]
b=[1,2,3]
c=['Life','is','too','short']
d=[1,2,'Life','is']
e=[1,2,['Life','is']] #list 안에 list 으로 들어가있다.
f=[1,2,['A','B',['C','D']]]
#리스트의 인덱싱
print(e[2])
print(e[-1][0],e[-1][1])
print(f[2][2][0]) #list 안에 list 안에 list 로 들어갔다.

#리스트의 슬라이싱
print(f[0:2])
print(f[:])
print(f[1:])
print(f[2][1:])
