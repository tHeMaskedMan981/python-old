
def isprime(a):
	
	for i in range (2,a):
		if a%i==0:
			return 0
			
	return 1		
	
def primebtw(m,n):
	
	for i in range (m,n+1):
		if (isprime(i)):
			print i 
			print '\n'
	return

t=input()

for x in range (0,t):
	m=input()
	n=input()
	primebtw(m,n)
	print '\n'
	
	
