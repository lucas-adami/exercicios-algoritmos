qtd = 1
soma_altura = 0
soma_peso = 0
maior_imc = float("-inf")
menor_imc = float("inf")

while qtd <= 20:
    altura = float(input(f"Digite a altura do {qtd}° indivíduo: "))
    peso = float(input(f"Digite o peso do {qtd}° indivíduo: "))

    imc = peso / pow(altura, 2)

    soma_altura = soma_altura + altura
    soma_peso = soma_peso + peso

    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc

    qtd += 1

print(f"O peso médio dos {qtd} indivíduos é de: {soma_peso / qtd}")
print(f"A altura média dos {qtd} indivíduos é de: {soma_altura / qtd}")
print(f"O maior IMC dentre os {qtd} indivíduos é de: {maior_imc}\nEnquanto o menor IMC é de: {menor_imc}")