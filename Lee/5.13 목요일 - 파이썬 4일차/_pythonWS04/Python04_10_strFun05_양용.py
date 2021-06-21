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


print("URL의 갯수 : ", len(a.split('?'))-1)
print("QueryString 갯수 : ", len(a.split('&')))