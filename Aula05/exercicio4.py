sexo = input("Informe seu sexo: ")
altura = float(input("Informe sua altura em metros: "))

if sexo.upper() == "HOMEM" or sexo.upper() == "H" or sexo.upper() == "MASCULINO":
    peso_ideal = float(72.7 * altura) - 58
    print(f"Seu peso certo é: {peso_ideal:.2f}")

elif sexo.upper() == "MULHER" or sexo.upper() == "M" or sexo.upper() == "FEMININO":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso certo é: {peso_ideal:.2f}")