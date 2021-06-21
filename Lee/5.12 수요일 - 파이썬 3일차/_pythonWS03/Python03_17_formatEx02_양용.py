'''
코드	설명
%s	문자열(String) ***
%c	문자 1개(character)
%d	정수(Integer) ***
%f	부동소수(floating-point) ***
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)
'''

print("%s" % "hi")
print("%10s" % "hi")
print("%-10s" % "hi")

print("%0.2f" % 3.1234321)
# 소숫점 이하 2자리까지
#소숫점 6자리가 디폴트
print("%5.2f" %3.123456789)
# 5는 최소 5줄까지 나오도록

