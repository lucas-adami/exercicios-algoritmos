from math import pow

i = 1
soma_altura = 0
soma_peso = 0
maior_imc = 0
menor_imc = 0

for i in range (1, 21):
    altura = float(input(f"Digite a altura da {i}° pessoa: "))
    peso = float(input(f"Digite o peso da {i}° pessoa: "))

    imc = peso/pow(altura, 2)

    soma_altura = soma_altura + altura
    soma_peso = soma_peso + peso

    if imc > maior_imc:
        maior_imc = imc
    elif imc < menor_imc:
        menor_imc = imc
    else:
        continue

print(f"O peso médio é de: {soma_peso/20} Kg.")
print(f"A altura média é de: {soma_altura/20} metro.")
print(f"O maior IMC é de: {maior_imc}, e o menor IMC é: {menor_imc}.")