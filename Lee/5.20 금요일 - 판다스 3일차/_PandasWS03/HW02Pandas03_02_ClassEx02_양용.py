class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second=second
a=FourCal()

#FourCal class에서 . setdata 라는 함수를 끌어와 (객체명,first숫자,second숫자)
FourCal.setdata(a,2,3)
print(a.first,a.second) #객체명.매개변수 / 여기에선 self가 a가 되는 것이다. = 객체명
# FourCal 클래스를 쓸 때, 매개변수 첫번째에 객체 이름을 반드시 넣어 주어야 한다.
print("="*50)

a.setdata(2,3) #이 경우는 객체를 앞에 a. 으로 쓰고 시작했으니까 ()안에 안넣어도 된다.
print(a.first, a.second)
