a="{2:<10}".format('aa','bb','cc')
b="{1:>10}".format('aa','bb','cc')
c="{:^10}".format('aa','bb','cc')
d="{:w^10}".format('aa','bb','cc')

print(a)
print(b)
print(c)
print(d)

x=123456789
y=1234.56789

w1="{0:,d}".format(x)

print(w1)
e1="{1:0.4f} {0:,d}".format(x,y)
#0.4f는 소숫점 4자리맞추기 그리고 ,d 는 3자리 끊기
e2="{0:20.3f}".format(y)
#20.3f는 토탈 20자리 맞추고 소숫점 3자리 맞추기

print(e1)
print(e2)