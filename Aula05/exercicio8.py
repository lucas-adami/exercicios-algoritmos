preco = float(input("Digite o preço do produto: "))
codigo_origem = int(input("Digite o código de origem: "))

if codigo_origem == 1:
    print(f"O produto é da região Sul e o valor final é de: R${preco * 1.11:.2f}")
elif codigo_origem == 2:
    print(f"O produto é da região Norte e o valor final é de: R${preco * 1.13:.2f}")
elif codigo_origem == 3:
    print(f"O produto é da região Nordeste e o valor final é de: R${preco * 1.09:.2f}")
elif codigo_origem == 4:
    print(f"O produto é da região Centro-Oeste e o valor final é de: R${preco * 1.12:.2f}")
elif codigo_origem == 5:
    print(f"O produto é da região Sudeste e o valor final é de: R${preco * 1.18:.2f}")