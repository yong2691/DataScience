'''
문제] 실행시 점수를 입력받아 80점 이상이면 "합격입니다."
         아니면, "다음기회에..."

'''

print("점수를 입력하세요.")
result=input()
#굳이 result=input() 을 여기서 할 필요는 없겠다.
print(result)

if int(result)>=85:
	print("합격입니다.")
else:
	print("다음기회에...")

'''
숫자열은 int()
문자열은 str()
'''

score=input()
if int(score)>=80:
	print("합격입니다.")
else:
	print("다음")