import random
from random import randint


def fermat_test(n, k):
    # True signifie "est peut être premier"

    # false signifie "composite"

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1, n - 1)

        if pow(a, n - 1) % n != 1:
            return False
    return True
n_1=int(input("donner le n: "))
k_1=int(input("donner le k: "))
if print(fermat_test(n_1,k_1))==True:
    print("est peut être premier")
else:
    print("composite")
