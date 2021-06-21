vI01=10
vI02=20
print(id(vI01))
print(id(vI02))

a=[1,2,3]
b=a
print(id(b))

print(a is b)

a[1]=7
print(a)
