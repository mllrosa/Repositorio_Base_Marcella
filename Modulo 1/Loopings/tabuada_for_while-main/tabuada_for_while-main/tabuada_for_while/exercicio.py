numero = int(input("Digite o numero para calcular a tabuada: "))
i = int(input("Digite o numero de onde iniciar a multiplicação da tabuada: "))
termino = int(input("Digite o numero de onde deve terminar a multiplicação tabuada: "))

while i <= termino:
     print(f" {i} x {numero} = {i * numero}")
     i += 1