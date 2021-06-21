'''
1. readline() 함수 이용하기
	- 첫 번째 줄 읽어 출력
2. readlines 함수 사용하기
	- 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
3. read 함수 사용하기
	- 파일의 내용 전체를 문자열로 돌려준다.
'''

# 1. readline() 함수 이용하기
f1=open("새파일.txt",'r')
line=f1.readline()
print(line)
f1.close()

#만약, 모든 줄을 읽어서 화면에 출력하고 싶다면,다음과 같이 작성하면된다.
f2=open("새파일.txt",'r')
while True:
	line=f2.readline()
	if not line:break
	print(line)
f2.close()

#반복문을 사용해서 readline을 돌리면, 첫째줄만 읽어서 출력하는게 아니고
# 반복하면서 그 다음 줄 그 다음 줄로 넘어가게 된다.