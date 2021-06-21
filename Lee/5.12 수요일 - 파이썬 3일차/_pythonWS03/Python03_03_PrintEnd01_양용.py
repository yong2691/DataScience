'''
for i in range(0, 5):
	print(i,end="\n") # end="\n" 은 옵션으로 들어가고 근데 이게 디폴트 값이라 쓰든 안쓰든 똑같다.

for i in range(0, 5):
	print(i,end="\t")


2단 3단을 2부터 출력해주세요
'''

for i in range(2,4):        # ①번 for문 아우터for문은 2바퀴
	for j in range(1, 4):   # ②번 for문 이너 for문은 3바퀴
		print(i*j, end=" ") 


#그럼 총 2단~3단까지 한단에 3개니까, 2 x 3= 6개가 나온다.