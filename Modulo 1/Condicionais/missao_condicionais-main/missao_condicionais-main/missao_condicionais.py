#1. Você está sendo avaliado(a) em sua habilidade de tomar decisões automatizadas por meio de códigos. Em cada uma das atividades a seguir, use estruturas condicionais com sabedoria.
#2. O Sistema de Avaliação da Agência Central de Inteligência precisa classificar os agentes de acordo com sua nota final. Sua missão é automatizar esse processo.
#Solicitar o nome do agente e sua nota final (0 a 10).
#Exibir a classificação:

nome_do_usuario = input('Ola! Seja bem-vindo ao Sistema de Avaliação da Agência Central de Inteligência, aqui, nosso trabalho é classificar os agentes. Por favor insira seu nome:')
nota = float(input('Por favor, digite sua nota final:'))

if 10.0 >= nota >= 9.0:
    print(f'Sr(a){nome_do_usuario}, sua nota foi Excelente 🏅')

elif 8.9 >= nota >= 7.0:
    print(f'Sr(a) {nome_do_usuario}, sua nota foi Boa 👍')

elif 6.9 >= nota >= 5.0:
    print(f'Sr(a) {nome_do_usuario}, sua nota foi Regular ⚠️')

elif 4.9 >= nota >= 3.0:
    print(f'Sr(a) {nome_do_usuario}, sua nota foi Ruim 🚫')

elif 2.9 >= nota >= 0.0:
    print(f'Sr(a) {nome_do_usuario}, sua nota foi Crítico 🚨')

else:
    print(f'Sr(a){nome_do_usuario}, sua nota foi Nota inválida ❌')

