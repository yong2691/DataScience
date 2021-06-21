class FourCal:

	def __init__(self): #__init__ 은 생성자이다.
#클래스의 이름과 동일하다고 취급한다.
		pass

	def __init__(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		result=self.first + self.second
		return result

	def sub(self):
		result=self.first-self.second
		return result
	
	def mul(self):
		result=self.first * self.second
		return result

	def div(self):
		result = self.first / self.second
		return result

class SafeFourCal(FourCal):
	def div(self):
		if self.second == 0: #이게 없는 상태에서 구동되면, 0으로 나눈값에서 에러가 뜬다.
			return 0
		else:
			#return super().div()      # super 없으면? 0이 아닌 숫자가 들어올때, 에러가 뜬다.
			return FourCal.div(self) #이렇게 써도 위에라인이랑 같은 결괏값이 나온다.
#a는 SafeFourCal의 객체를 상속 하니까, 29번 먼저 실행하는 것이다.
# 0이 아니면? 32번라인에서 super로 인해 상위값으로 간다.
#상위class으로 가기 위해서는? super()


a = SafeFourCal(4,1)

print(a.first,"+",a.second,"=",a.sum())
print(a.first,"-",a.second,"=",a.sub())
print(a.first,"*",a.second,"=",a.mul())
print(a.first,"/",a.second,"=",a.div())
