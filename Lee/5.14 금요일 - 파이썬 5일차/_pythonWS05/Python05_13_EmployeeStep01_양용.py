# 사번, 이름, 입사일, 급여
# 계약직, 정규직
# 사번 1번째
# T,t << 계약직
# R << 정규직

TName = ["구분","사원명","입사일","급여"]
empInfo = [
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]
empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]

print("%-10s" %TName[0],"%-10s" %TName[1],"%-10s" %TName[2],"%-15s" %TName[3])
print("-"*50)

a=empInfo
for i in range(0,len(empInfo)):
	a[i].append(empPayTable[i])


for n in range(0,len(empInfo)):
	if a[n][0][0]=="T"or a[n][0][0]=="t":
		print("%-10s" %"계약직","%-10s" %a[n][1],"%-15s" %a[n][2],"{0:<10,d}".format(a[n][3][0]*a[n][3][1]))
	elif a[n][0][0]=="R" or a[n][0][0]=="r":
		print("%-10s" %"정규직","%-10s" %a[n][1],"%-15s" %a[n][2],"{0:<10,d}".format(a[n][3][0]*a[n][3][1]))	

''' 포맷함수 참고참고
x=123456789
y=1234.56789
w1="{0:,d}".format(x)
w1="{0:<10,d}".format(x)

for n in range(0,len(empInfo))
	del empInfo[0]

print(TName[0],"     ",TName[1],"     ",TName[2],"     ",TName[3],"     ")
print("-"*50)
for i in range(len(empInfo)):
	print(empInfo[i][0],"     ", empInfo[i][1],"     ",empInfo[i][2],"     ", empPayTable[i][0]*empPayTable[i][1])

print("-"*50)
'''