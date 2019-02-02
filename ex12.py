mano=int(input(""))
temp=mano
r=0
while(mano>0):
	d=mano%10
	r=r*10+d
	mano=mano//10
if(temp==r):
	print('yes')
else:
	print('no')
 
