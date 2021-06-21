'''
a=[1,2,3,4]
result=[num*3 for num in a if num%2==0]
print(result)

result=[x*y for x in range(2,10) for y in range(1,10)]
print(result)


%s 문자열 string
%d 

코드	설명
%s	문자열(String) ***
%c	문자 1개(character)
%d	정수(Integer) ***
%f	부동소수(floating-point) ***
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)
'''
'''
print("Error is %d" %98)
print("i had %s apples" %3)
print("i gave you %f dollars" %3.22533)

'''

menu=['o','p']
print(menu[0],menu[1])
print(menu[1],menu[0])