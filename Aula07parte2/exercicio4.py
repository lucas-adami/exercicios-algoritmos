qtd = 1
soma_idade = 0

while True:

    idade = int(input(f"Digite a idade do {qtd}º indivíduo: "))

    if idade > 0:
        soma_idade = soma_idade + idade
        media = soma_idade / qtd

        print(f"A idade média de todos os {qtd} indivíduos é de: {media}")

        qtd += 1
    else:
        break