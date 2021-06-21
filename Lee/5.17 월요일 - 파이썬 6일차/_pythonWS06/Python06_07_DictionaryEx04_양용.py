#딕셔너리 관련 함수들, key 리스트 만들기(keys)
#keys 함수 사용법은? a.keys()

a={'name':'yong', 'phone':2691,'birth':'0222'}
print(a.keys())

#dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도
#기본적인 반복(iterate) 구문(예:for문)을 실행 할 수 있다.

for i in a.keys():
	print(i)

#dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
vList=list(a.keys())
#이렇게하면 딕셔너리 키들이 리스트로 변환이 된다.
print(vList) 