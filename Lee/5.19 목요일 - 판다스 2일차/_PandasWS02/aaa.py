class Fourcal:
	def setdata(self, first, second): #setdata는 함수 / self, first, second는 속성
		self.first=first
		self.second=second

a= Fourcal() #객체 생성 = 클래스는 객체 생성 후 사용 한다.
a.setdata(4,2)

print(a.first) # a객체안에있는 first를 출력
print(a.second) #사용할때는 객체.속성 a는 객체 second는 속성
print(type(a))