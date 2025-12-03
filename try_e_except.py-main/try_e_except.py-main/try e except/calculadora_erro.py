
print("CALCULADORA")

while True:
    try:

        print("Qual a proxima operação?")
        print("1 - ADIÇÃO")
        print("2 - SUBTRAÇÃO")
        print("3 - MULTIPLICAÇÃO")
        print("4 - DIVISÃO")

        codigo = int(input())

        match codigo:
                case 1:
                    print("Para realizar a ADIÇÃO digite os numeros:")
                    numero_adi1 = int(input("O primero numero: "))
                    numero_adi2 = int(input("O segundo numero: "))
                    soma = numero_adi1 + numero_adi2
                    print(f"O resultado é {soma}")

                case 2:
                    print("Para realizar a subtração digite os numeros:")
                    numero_sub1 = int(input("O primero numero: "))
                    numero_sub2 = int(input("O segundo numero: "))
                    subtracao = numero_sub1 - numero_sub2
                    print(f"O resultado é {subtracao}")

                case 3:                                                                                                                                                                                                                                                                                                                                            
                    print("Para realizar a multiplicação digite os numeros:")
                    numero_mul1 = int(input("O primero numero: "))
                    numero_mul2 = int(input("O segundo numero: "))
                    multiplicacao = numero_mul1 * numero_mul2
                    print(f"O resultado é {multiplicacao}")

                case 4:
                    print("Para realizar a divisão digite os numeros:")
                    numero_div1 = int(input("O primero numero: "))
                    numero_div2 = int(input("O segundo numero: "))
                    divisao = numero_div1 / numero_div2
                    print(f"O resultado é {divisao}")

    except:
        print("Tente novamente e digite os números corretamente!")