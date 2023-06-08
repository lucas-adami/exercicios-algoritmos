from datetime import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = datetime.now().year - ano_nascimento

if idade >= 18:
    print("Você já pode sua CNH!")
else:
    if idade >= 16:
        print("Você já pode votar!")
    else:
        print("Você ainda é menor de idade...")