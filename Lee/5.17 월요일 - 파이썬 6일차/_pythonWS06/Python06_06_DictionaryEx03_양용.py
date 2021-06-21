
dic={'name':'yong', 'phone':'010',3:'0222'}
print(dic['name'])
print(dic['phone']) # 딕셔너리에서 'phone' 이라는 key값 출력
print(dic[3]) # 딕셔너리에서 3이라는 key값 출력

a={1:'b',1:'c'} #딕셔너리에서는 key값이 중복되면 안된다고 했는데,
print(a)  #만약 중복이 되면? 뒤엣 값을 불러오게 된다. Overwrite 라고 부른다.