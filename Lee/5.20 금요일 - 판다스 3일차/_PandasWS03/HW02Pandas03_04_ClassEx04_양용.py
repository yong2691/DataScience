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

#a= FourCal()
#a.setdata(4,2) #self라는 객체에 4하고 2가 들어간 것이다.

a=FourCal(4,2)

print(a.first,"+",a.second,"=",a.sum())
print(a.first,"-",a.second,"=",a.sub())
print(a.first,"*",a.second,"=",a.mul())
print(a.first,"/",a.second,"=",a.div())

