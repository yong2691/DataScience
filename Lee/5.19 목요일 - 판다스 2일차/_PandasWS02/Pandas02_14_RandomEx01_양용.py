import random

for i in range(5): # i : 0 1 2 3 4
	print("%0.3f" %random.random())

print("="*50)

for i in range(5):
	print("%d" %random.randint(1,3))

print("="*50)

for i in range(5):
	print("%d" %random.randint(1,45), end=' ')
	print()
print("="*50)