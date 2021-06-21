'''
for i in range(0, 5):
	print(i,end="\n") # end="\n" 은 옵션으로 들어가고 근데 이게 디폴트 값이라 쓰든 안쓰든 똑같다.

for i in range(0, 5):
	print(i,end="\t")


2단 3단을 2부터 출력해주세요
'''

for i in range(2,4):        # ①번 for문 아우터for문은 2바퀴
	for j in range(1, 4):   # ②번 for문 이너 for문은 3바퀴
		print(i*j, end=" ")  # 라인 변경(개행) 없다. 이걸 왜 했냐? 기본 default 값으로 end"\n" 으로 되어 있으니까, end"" 이렇게 하면 \n 이 빠지는 거다.
	print('') # 라인 변경(개행)

# end="" 은 뭐냐? 기본값인 \n 을 무시하는 것이다.
# end="" 은 그냥 바로 옆에 출력되고
# end=" " 은 한칸 띄어서 바로 옆에 출력되고
# end="  " 은 두칸 띄어서바로 옆에 출력되고
#그럼 총 2단~3단까지 한단에 3개니까, 2 x 3= 6개가 나온다.