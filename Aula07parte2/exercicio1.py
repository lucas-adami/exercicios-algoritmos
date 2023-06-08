e = 0
b = int (input ("Digite o valor da base: "))
n = int (input ("Digite um número inteiro: "))
i = 1

while (i <= n):
    e = e + b ** i
    i += 1

print(f"E = {e:.2f}")