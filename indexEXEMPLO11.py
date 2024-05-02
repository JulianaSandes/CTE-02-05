L = []
while True:
 num = int(input("Digite um número (0 sai): "))
 if num == 0:
  break
 L.append(num)
x = 0
while x < len(L):
 print(L[x])
 x += 1
print(L)
L.sort() #o método sort sem argumento ordena a lista em ordem ascendente
print(L)
L.sort(reverse=True) #o método sort com argumento reverse=True ordena a lista
#em ordem descendente
print(L)