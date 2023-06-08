num = int(input("Digite um número inteiro e positivo: "))
fatorial = 1

for i in range(num, 0, -1):
    fatorial *= i

print(f"O valor do fatorial deste número é de {fatorial}")