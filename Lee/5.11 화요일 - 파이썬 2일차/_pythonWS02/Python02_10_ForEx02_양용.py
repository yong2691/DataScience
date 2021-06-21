marks = [90, 80, 70 , 60, 50]
number=0
for mark in marks:
	number = number + 1
	if mark >= 70:
		print(number,"번 학생은 합격입니다.")
	else:
		print(number,"번 학생은 불합격입니다.")