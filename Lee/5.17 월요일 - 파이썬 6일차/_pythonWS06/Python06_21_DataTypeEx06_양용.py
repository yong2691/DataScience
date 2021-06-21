vI01=20
vI02=30

print("교환전 값:", vI01, vI02)
temp=vI01 # temp를 프린트하면 오른쪽 값이 출력된다.
vI01=vI02 # vI01을 프린트하면 오른쪽 값이 출력된다.
vI02=temp # vI02를 프린트하면 오른쪽 값이 출력된다.
print("교환전 값:", vI01,vI02)

a=3
b=5
print("교환전 값:",a,b)
a,b=b,a #앞뒤를 바꾸는 중
print("교환후 값:",a,b)