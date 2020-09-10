def gcd(a,b):
	if(a<b):
		a,b=b,a

	if(a==0 or b==0):
		return a+b
	elif(a%b==0):
		return b
	else:
		return gcd(a%b,b)