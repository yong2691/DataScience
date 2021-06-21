#리스트 요소 제거 (remove)_ 첫 번째 3만 제거

a=[1,2,3,1,2,3]
result1=a.remove(3)
print(result1)
print(a)
print("-"*15)

#remover는 제거하는데, 제거만 하고 반환은 안해준다.
#pop은 제거하는데, 제거 하는 것도 반환을 해준다.

a=[1,2,3]
result2=a.pop()
print(result2)
print(a)
print("-"*15)

a=[1,2,3,1,2,3]
del a[5]
print(a)
print("-"*15)

#파이썬을 기본으로 해서 만들어진게 넘파이와 판다스