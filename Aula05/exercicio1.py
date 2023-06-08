num1 = float(input("Insira um número: "))
num2 = float(input("Insira um número: "))

if num1 == num2:
    print(f"Voce digitou 2 numeros iguais")
else:
    if num1 < num2:
       print(f"O numero {num1} é o menor entre os 2")
    else:
        print(f"O numero {num2} é o menor entre os 2")