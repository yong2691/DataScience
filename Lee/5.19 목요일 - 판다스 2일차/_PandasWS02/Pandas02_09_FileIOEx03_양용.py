'''
1. readline() 함수 이용하기
	- 첫 번째 줄 읽어 출력
2. readlines 함수 사용하기
	- 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
3. read 함수 사용하기
	- 파일의 내용 전체를 문자열로 돌려준다.
'''

#2. readlines 함수 사용하기

f=open("새파일.txt",'r')
lines=f.readlines()
print(lines) #파일 안에 들어있는 모든줄을 list 문자열 형태로 돌려준다.

for line in lines:
	print(line)
	#print의 디폴트값이 \n 이 포함되어 라인개행이된다.
	#그러니까 for문을 돌 때 라인개행이 기본 하나씩 되어서 나오는 것이다.
	#디폴트값\n + 우리가 써준 \n 되어서 두칸 띄어서 결과값이 프린트 된다.!

f.close()
