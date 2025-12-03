# 📝 PROJETO 07 — Registro de Participantes em Evento
# Crie um sistema simples para cadastrar participantes com nome, e-mail e CPF.
# Ao final, exiba a quantidade total de inscritos.

def cadastrar_participante():
    """Cadastra um novo participante no evento"""
    print("\n" + "="*50)
    print("📝 CADASTRO DE PARTICIPANTE")
    print("="*50)
    
    nome = input("Nome completo: ").strip()
    email = input("E-mail: ").strip()
    cpf = input("CPF (apenas números): ").strip()
    
    # Validações básicas
    if not nome:
        print("❌ Nome é obrigatório!")
        return None
    
    if not email or "@" not in email:
        print("❌ E-mail inválido!")
        return None
    
    if not cpf or len(cpf) != 11 or not cpf.isdigit():
        print("❌ CPF deve conter 11 números!")
        return None
    
    participante = {
        'nome': nome,
        'email': email,
        'cpf': cpf
    }
    
    print(f"✅ Participante {nome} cadastrado com sucesso!")
    return participante

def exibir_participantes(participantes):
    """Exibe todos os participantes cadastrados"""
    if not participantes:
        print("\n📭 Nenhum participante cadastrado ainda.")
        return
    
    print("\n" + "="*60)
    print("👥 LISTA DE PARTICIPANTES CADASTRADOS")
    print("="*60)
    
    for i, participante in enumerate(participantes, 1):
        print(f"{i:2d}. {participante['nome']} | {participante['email']} | CPF: {participante['cpf']}")

def main():
    """Função principal do sistema"""
    participantes = []
    
    print("🎉 BEM-VINDO AO SISTEMA DE REGISTRO DE PARTICIPANTES!")
    
    while True:
        print("\n" + "-"*50)
        print("📋 MENU PRINCIPAL")
        print("-"*50)
        print("1. Cadastrar novo participante")
        print("2. Listar todos os participantes")
        print("3. Ver quantidade total de inscritos")
        print("4. Sair do sistema")
        
        opcao = input("\nEscolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            participante = cadastrar_participante()
            if participante:
                participantes.append(participante)
                
        elif opcao == "2":
            exibir_participantes(participantes)
            
        elif opcao == "3":
            print(f"\n📊 TOTAL DE INSCRITOS: {len(participantes)} participante(s)")
            
        elif opcao == "4":
            print(f"\n🎯 RESUMO FINAL:")
            print(f"📊 Total de inscritos: {len(participantes)}")
            print("👋 Obrigado por usar nosso sistema! Até logo!")
            break
            
        else:
            print("❌ Opção inválida! Por favor, escolha entre 1 e 4.")

# Executa o programa
if __name__ == "__main__":
    main()