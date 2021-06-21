# Key로 Value 얻기 (get)

a={'name':'yong','phone':'2691','birth':'0222'}
print(a.get('name'))

'''
get(x) 함수는 x라는 key에 대응되는 Value를 돌려준다.
a['nokey']는 Key 오류를 발생시키고
a.get('nokey')는 None으로 돌려준다는 차이가 있다.
'''
print(a.get('nokey'))
# print(a['nokey']) #KeyError

'''
딕셔너리 안에 찾으려는 Key값이 없을 경우 미리 정해둔 디폴트 값을 대신
가져오게 하고 싶을 때에는 get(x,'디폴트값')을 사용하면 편리하다.
a 딕셔너리에는 'foo'에 해당하는 값이 없다.
따라서 디폴트 값인 'bar'를 돌려준다.
'''
a={'name':'yong','phone':'2691','birth':'0222'}
print(a.get('foo','rr'))

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
#있는지 없는지만 확인하는 것이다.

a={'name':'yong','phone':'2691','birth':'0222'}
print('name' in a)
print('email' in a)