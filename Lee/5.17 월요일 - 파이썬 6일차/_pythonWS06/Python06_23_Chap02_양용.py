#Q1 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.
print("Q1","-"*50)

sublist=['국어','영어','수학']
score=['80','75','55']

n=int(0)
for i in range(len(score)):
	n=n+int(score[i])

print("홍길동의 평균점수 : ", n/len(score))

print("Q2","-"*50)
#Q2 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.

while True:
	n=int(input("숫자를 입력하세요."))
	if n%2 == 1 :
		print(n,"은 홀수입니다.")
	elif n%2==0:
		print(n,"은 짝수입니다.")
	break
print("Q3","-"*50)
#Q3 홍길동 씨의 주민등록번호는 881120-1068234이다.
#홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

n=["881120-1068234"]

print("19",end="")
print(n[0][0:6])
print(n[0][8:])
print("Q4","-"*50)
#Q4 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다.
# 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = ['881120-1068234']
if pin[0][7] == '1' or pin[0][7] == '3' :
	print("남자입니다.")
elif pin[0][7] == '2' or pin[0][7] == '4' :
	print("여자입니다.")
print("Q5","-"*50)
#Q5 다음과 같은 문자열 a:b:c:d가 있다.
#문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

a="a:b:c:d"
a.replace(":","#")
print(a)
print("Q6","-"*50)
#Q6 [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
print("Q7","-"*50)
#Q7 ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
a=['Life', 'is', 'too', 'short']
for i in range(len(a)):
	print(a[i],end=" ")
print("\n")
print("Q8","-"*50)
#Q8 (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
a=(1,2,3)
a=a+(4,)
print(a)
print("Q9","-"*50)
#Q9 다음과 같은 딕셔너리 a가 있다.

'''
>>> a = dict()
>>> a
{}
다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.

a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python'
a[250] = 'python'
'''
a=dict()
a['name']='aa'
a[('a',)]='bb'
a[[1]]='cc' #여기에서 에러가 난다.
#왜냐면 딕셔너리 안에 [1] 라는 리스트가 들어갔으니까,
#딕셔너리는 변하는 값을 사용할 수 없다.
a[250]='dd'
print(a)

print("-"*50)

