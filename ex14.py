a=input()
b=a.split()
c=int(b[0])
d=int(b[1])
if c and d <=100000:
	for e in range(c+1,d):
		if e%2 ==1:
			print(e)		
