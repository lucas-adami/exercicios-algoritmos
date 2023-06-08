idade_nadador = int(input("Insira a idade do nadador: "))

if idade_nadador > 30:
    print("A sua categoria é a Senior")
elif 15 < idade_nadador < 31:
    print("Sua categoria é Adulto!")
elif 10 < idade_nadador < 16:
    print("Sua categoria é a Adolescente")
elif 7 < idade_nadador < 11:
    print("Sua categoria é a Juvenil")
else:
    print("Sua categoria é a infatil")
