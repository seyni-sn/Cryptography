import random

def appartient(alpha,n,h):
    t=int(input("donner un nombre impair :"))
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
a=int(input("donner alpha :"))
b=int(input("donner n :"))
c=int(input("donner h :"))
print(appartient(a,b,c))
