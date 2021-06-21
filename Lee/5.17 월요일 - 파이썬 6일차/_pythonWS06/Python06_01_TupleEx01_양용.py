#튜플 요솟값을 삭제하려 할 때
t1=(1,2,'a','b')
print(t1[0])

# del t1[0]    #삭제 시 Error 발생
# TypeError: 'tuple' object doesn't support item deletion
# 튜플에서는 삭제를 지원하지 않는다.
t1[0] = 'c'   # 변경 시 Error 발생

# 인덱싱하기
t1=(1,2,'a','b')
print(t1[0])
print(t1[3])

#슬라이싱하기
print(t1[1:])
print("*"*10)