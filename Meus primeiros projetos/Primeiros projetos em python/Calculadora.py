print("-=-" * 11)
print("Bem-vindo a calculadora em python")
print("-=-" * 11)

print(" _____________________ ")
print("|  _________________  |")
print("| |               0 | |")
print("| |_________________| |")
print("|  ___ ___ ___   ___  |")
print("| | 7 | 8 | 9 | | + | |")
print("| |___|___|___| |___| |")
print("| | 4 | 5 | 6 | | - | |")
print("| |___|___|___| |___| |")
print("| | 1 | 2 | 3 | | x | |")
print("| |___|___|___| |___| |")
print("| | . | 0 | = | | ÷ | |")
print("| |___|___|___| |___| |")
print("|_____________________|")
print("")
print("● [1] Calculadora de soma")
print("● [2] Calculadora de subtração")
print("● [3] Calculadora de multiplicação")
print("● [4] Calculadora de divisão")
print("")

while True:

    tipoCalculadora = int(
        input("Qual operação você deseja realizar [1], [2], [3] ou [4]?"))

    if tipoCalculadora == 1:
        num1 = float(input("Digite o primeiro número que deseje somar:"))
        num2 = float(input("Digite o segundo número que deseje somar:"))
        sumResult = num1 + num2
        print(f"A soma de {num1} + {num2} é igual a: {sumResult}")

    elif tipoCalculadora == 2:
        num1 = float(input("Digite o primeiro número que deseje subtrair:"))
        num2 = float(input("Digite o segundo número que deseje subtrair:"))
        subResult = num1 - num2
        print(f"A sbutração de {num1} - {num2} é igual a: {subResult}")

    elif tipoCalculadora == 3:
        num1 = float(input("Digite o primeiro número que deseje multiplicar:"))
        num2 = float(input("Digite o segundo número que deseje multiplicar:"))
        mulResult = num1 * num2
        print(f"A multiplicação de {num1} * {num2} é igual a: {mulResult}")

    elif tipoCalculadora == 4:
        num1 = float(input("Digite o primeiro número que deseje dividir:"))
        num2 = float(input("Digite o segundo número que deseje dividir:"))
        if num1 == 0:
            print("ERRO! Divisão por 0 é inexistente")
        elif num2 == 0:
            print("ERRO! Divisão por 0 é inexistente")
        else:
            divResult = num1 / num2
            print(f"A divisão de {num1} / {num2} é igual a: {divResult}")

    else:
        print("Escolha invalida, por favor escolha um número entre [1] e [4]")

    jogarNovamente = str(input("Você deseja calcular novamente? s/n: ").lower())
    if jogarNovamente == "n":
        print("Obrigado por usar nossa calculadora!")
        break
