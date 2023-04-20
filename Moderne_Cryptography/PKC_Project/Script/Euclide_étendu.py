def euclide_etendu(a,b):
  x = 1 ; xx = 0
  y = 0
  yy = 1
  while b != 0:
      q = a // b
      a , b = b, a % b
      xx , x = xx, x - q * xx
      yy, y = y - q * yy, yy
  return a, x ,y
# retourne le pgcd ainsi que les coefficients u et v de Bézout
c1=int(input("donner a :"))
c2=int(input("donner b :"))
print(euclide_etendu(c1,c2))

