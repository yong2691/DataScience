'''
딕셔너리 쌍 추가하기
a[2]='b'와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각
2와 'b'인 2 : 'b' 라는 딕셔너리 쌍이 추가 된다.
'''

a={1:'a'}
a[2]='b'
print(a)

a['name']='yong'
print(a)

del a['name']
print(a)