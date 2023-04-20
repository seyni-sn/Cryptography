
import random

def Ln(alpha,n,h):
    
    t = 3
    beta=pow(alpha,t)%n
    if beta == 1:
        return True

    for i in range(h):
        if beta == -1:
            return True
        if beta == 1:
            return True

        beta=pow(beta,2)%n
    return False



def millerRabin(n,k):
	if n  == 2:
		return True
	if n%2 == 0:
		return False
	for i in range(k):
		 alpha = random.randint(1,n-1)
		 if Ln(alpha,n,k)!=True:
		 	return False
	return True
	
n = 7; k = 10
print(millerRabin(n,k))

