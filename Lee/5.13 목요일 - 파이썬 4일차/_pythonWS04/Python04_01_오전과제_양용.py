'''
Q1
홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.

과목	점수
국어	80
영어	75
수학	55
'''

score = [80,75,55]

sum=0
for i in score:
	sum=sum+i
print(sum/len(score))

'''
Q2
자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해말해 보자.
'''

num=13
if num%2==0:
	print("짝수")
else:
	print("홀수")