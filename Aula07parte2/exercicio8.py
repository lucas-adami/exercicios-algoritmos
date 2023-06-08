numero = int(input("Digite um número inteiro maior 1: "))

i = 2

if numero <= 1:
    primo = "não é um número primo"
else:
    primo = "é primo."

while i <= int(numero ** 0.5):
    if numero % i == 0:
        primo = "não é primo."
        break
    i += 1

print(f"O número {numero} {primo}")