while True:
    x = int (input ("Digite um número inteiro: "))
    if x >= 0:
        break
    print("Valor inválido. O numero digitado é menor ou igual a zero.")

fatorial = 1
i = 2
while i <= x:
     fatorial = fatorial * i
     i += 1

print(f"O valor de {x}! é igual a {fatorial}")