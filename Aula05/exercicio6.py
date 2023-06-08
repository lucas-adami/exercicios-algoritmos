num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

media = (num1 + num2) / 2

print(f"A média entre os 2 numeros apresentados é {media}")

if num1 == num2:
    print(f"Os 2 numeros são iguais")
else:
    if num1 > num2:
        print(f"A diferença entre eles é {num1 - num2}")
    else:
        print(f"A diferença entre eles é {num2 - num1}")

print(f"O produto entre os 2 numeros apresentados é {num1 * num2}")
print(f"A divisão do primeiro numero com o segundo é igual a {num1 / num2}")