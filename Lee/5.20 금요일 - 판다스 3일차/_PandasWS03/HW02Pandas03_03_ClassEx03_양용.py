class FourCal:
	def setdata(self,first,second):
		self.first=first
		self.second=second

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

a= FourCal()
a.setdata(4,2) #self라는 객체에 4하고 2가 들어간 것이다.


print(a.first,"+",a.second,"=",a.sum())
print(a.first,"-",a.second,"=",a.sub())
print(a.first,"*",a.second,"=",a.mul())
print(a.first,"/",a.second,"=",a.div())

