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