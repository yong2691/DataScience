# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() #vartest 라는 함수를 한번 가동 연산 한 것이다. 
print(a)