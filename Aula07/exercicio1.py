import math
e = 0
n = int(input("Digite um numero inteiro e positivo: "))
for i in range(1, n+1):
    e = e + math.pow(2, i)
    print(i)
print(f'O valor de E = {e:.2f}')