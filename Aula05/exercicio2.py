nota1 = float(input("Insira a 1° nota do aluno: "))
nota2 = float(input("Insira a 2° nota do aluno: "))
nota3 = float(input("Insira a 3° nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if media < 3.0:
    print("Infelizmente você foi reprovado")
else:
    if media > 3.0 and media < 7.0:
        print("Você vai precisar fazer uma prova de recuperação")
    else:
        print("parabens voce passou de ano")