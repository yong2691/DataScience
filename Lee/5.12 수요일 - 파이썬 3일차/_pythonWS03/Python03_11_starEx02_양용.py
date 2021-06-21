for i in range(5,0,-1):
	for j in range(0,i):
		print("*",end="")
	print('')

'''
             outer i    inner j
*               1             1    
**             2            2
***           3            3
****         4            4
*****       5            5
'''
'''
             outer i    inner j
*****       1            5
****         2            4
***           3            3
**             4            2
*               5             1    
'''