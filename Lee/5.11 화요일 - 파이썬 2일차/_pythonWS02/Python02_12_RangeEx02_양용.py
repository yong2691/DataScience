marks=[90,80,70]

number=0
for mark in marks:
	number=number+1
	if mark >= 60:
		print(number,"번 학생은 합격입니다.")
	else:
		print(number,"번 학생은 불합격입니다.")


marks=[90,80,70,60,50]

print(marks[0])
print(marks[1])
print(marks[4])
