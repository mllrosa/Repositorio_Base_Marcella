#1. nome do cliente
nome_do_cliente = input('Seja bem vido! Qual o seu nome por favor?')

#2. endereço
endereço = input("Endereço de entrega:")

#3. receber o pedido
pedido = input('Digite qual o sabor da sua pizza: \n''(Mussarela | Calabresa | Portuguesa | Marguerita):')

print(f'Sr.{nome_do_cliente}, seu pedido será entregue no {endereço}, o sabor escolhido é {pedido}')

#4. opções (elif tradução para pt-br senão então)

if pedido == "Mussarela":
    print(f'Sr(a) {nome_do_cliente}, o seu pedido será entregue no {endereço}, sabor escolhido é: {pedido}')
elif pedido == "Calabresa":
    print(f'Sr(a) {nome_do_cliente}, o seu pedido será entregue no {endereço}, sabor escolhido é: {pedido}')
elif pedido == "Portuguesa":
    print(f'Sr(a) {nome_do_cliente}, o seu pedido será entregue no {endereço}, sabor escolhido é: {pedido}')
else:
    print(f'Sr(a) {nome_do_cliente}, o seu pedido será entregue no {endereço}, sabor escolhido é: {pedido}')

