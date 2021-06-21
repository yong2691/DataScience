
add = 0 
for i in range(1, 11): #for문에서 i라는 변수는 1~10까지 돌것이다.
	add = add + i
	print(add)

print("1~10까지의합:",add)


#1~10까지의 홀수합

odd=0
for ii in range(1,11,2):
	odd=odd+ii

print("1~10까지의 홀수합:",odd)

#1~10까지의 짝수합

even=0
for iii in range(2,11,2):
	even=even+iii

print("1~10까지의 짝수합:",even)