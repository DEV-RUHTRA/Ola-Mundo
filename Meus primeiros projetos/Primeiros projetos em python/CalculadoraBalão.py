print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
print("|Bem-vindo a calculadora de balões|")
print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
numerodebaloes = 100

while True:

    qtdArcos = int(input("• Quantos arcos você deseja?"))
    qtdCores = int(input("• Quantas cores diferentes você deseja?"))
    qtdbalões = qtdArcos * numerodebaloes
    baloesPorCor = qtdbalões // qtdCores

    print(f"A quantidade aproximada necessaria de balões por cor é igual a: {
        baloesPorCor}")

    jogarNovamente = str(input("Deseja calcular novamente? s/n: ").lower())
    if jogarNovamente == "n":
        print("Obrigado por usar nossa calculadora!")
        break
