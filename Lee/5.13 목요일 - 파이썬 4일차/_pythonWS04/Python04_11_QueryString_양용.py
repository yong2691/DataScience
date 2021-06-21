'''
https://search.naver.com/search.naver?
where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python

앞단은 URL 이라고 하고
뒷단은 QueryString 이라고 한다.
&을 기준으로 QueryString은 5개 이다.
	where=nexearch
	sm=top_hty
	fbm=1
	ie=utf8
	query=python
QueryString 개수 : 5개
'''
a="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python"
print(a.split('&'))
b=a.split('&')
print(b[1])
print(a.split('&')[1])
for i in range(0,len(b)):
	print(b[i])

print("QueryString 갯수 : ", len(a.split('&')))
print("URL의 갯수 : ", len(a.split('?'))-1)

# 함수란??
# 1. 명령어들의 집합을 묶어준거
# 2. 함수 이름이 소괄호()로 되어져있고
# 3. 
# 재사용 하기 위한것.

# 문자 / 숫자 구분 하는법?
# 1. 연산유무
# 2. " " 또는 ''쓰면 숫자도 문자가 된다.
# ex: "10" 은 문자이다.
# 3. 주석을 달때는 ''' ''' 또는 """ """