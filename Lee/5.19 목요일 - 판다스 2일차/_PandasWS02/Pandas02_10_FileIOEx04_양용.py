'''
1. readline() 함수 이용하기
	- 첫 번째 줄 읽어 출력
2. readlines 함수 사용하기
	- 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
3. read 함수 사용하기
	- 파일의 내용 전체를 문자열로 돌려준다.
'''

#3. read 함수 사용하기

f=open("새파일.txt",'r')
data=f.read()
print(data) #print 될 때, 기본적으로 \n이 디폴트되어 있어 라인개행 들어간다.
f.close()