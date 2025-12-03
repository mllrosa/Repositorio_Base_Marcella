# 📇 PROJETO 08 — Lista de Contatos (While)
# Monte uma lista de contatos com laços while e opções de adicionar, listar e remover.

# O programa só termina quando o usuário escolher “sair”.

# 📇 PROJETO 08 — Lista de Contatos (While)

def main():
    lista_contatos = []
    
    print("📇 SISTEMA DE LISTA DE CONTATOS")
    print("=" * 40)
    
    while True:
        # Menu principal
        print("\n📋 MENU PRINCIPAL")
        print("1. 👥 Listar contatos")
        print("2. ➕ Adicionar contato")
        print("3. ❌ Remover contato")
        print("4. 🔍 Buscar contato")
        print("5. 🚪 Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            listar_contatos(lista_contatos)
            
        elif opcao == "2":
            adicionar_contato(lista_contatos)
            
        elif opcao == "3":
            remover_contato(lista_contatos)
            
        elif opcao == "4":
            buscar_contato(lista_contatos)
            
        elif opcao == "5":
            print("\n👋 Obrigado por usar o sistema!")
            print(f"📊 Total de contatos salvos: {len(lista_contatos)}")
            break
            
        else:
            print("❌ Opção inválida! Escolha entre 1 e 5.")

def listar_contatos(contatos):
    """Lista todos os contatos cadastrados"""
    print("\n👥 LISTA DE CONTATOS")
    print("=" * 50)
    
    if not contatos:
        print("📭 Nenhum contato cadastrado.")
        return
    
    for i, contato in enumerate(contatos, 1):
        print(f"{i:2d}. {contato['nome']} - 📞 {contato['telefone']} - 📧 {contato['email']}")

def adicionar_contato(contatos):
    """Adiciona um novo contato à lista"""
    print("\n➕ ADICIONAR NOVO CONTATO")
    print("-" * 30)
    
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    
    # Validações básicas
    if not nome:
        print("❌ Nome é obrigatório!")
        return
    
    if not telefone:
        print("❌ Telefone é obrigatório!")
        return
    
    # Verifica se o telefone já existe
    for contato in contatos:
        if contato['telefone'] == telefone:
            print("❌ Já existe um contato com este telefone!")
            return
    
    novo_contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    
    contatos.append(novo_contato)
    print(f"✅ Contato '{nome}' adicionado com sucesso!")

def remover_contato(contatos):
    """Remove um contato da lista"""
    if not contatos:
        print("📭 Nenhum contato para remover.")
        return
    
    listar_contatos(contatos)
    
    try:
        numero = int(input(f"\nDigite o número do contato a remover (1-{len(contatos)}): "))
        
        if 1 <= numero <= len(contatos):
            contato_removido = contatos.pop(numero - 1)
            print(f"✅ Contato '{contato_removido['nome']}' removido com sucesso!")
        else:
            print("❌ Número inválido!")
            
    except ValueError:
        print("❌ Digite um número válido!")

def buscar_contato(contatos):
    """Busca contatos por nome"""
    if not contatos:
        print("📭 Nenhum contato cadastrado.")
        return
    
    termo = input("\n🔍 Digite o nome para buscar: ").strip().lower()
    
    if not termo:
        print("❌ Digite um termo para buscar!")
        return
    
    contatos_encontrados = []
    
    for contato in contatos:
        if termo in contato['nome'].lower():
            contatos_encontrados.append(contato)
    
    print(f"\n🔍 RESULTADOS DA BUSCA por '{termo}'")
    print("=" * 50)
    
    if not contatos_encontrados:
        print("❌ Nenhum contato encontrado.")
        return
    
    for i, contato in enumerate(contatos_encontrados, 1):
        print(f"{i:2d}. {contato['nome']} - 📞 {contato['telefone']} - 📧 {contato['email']}")

# Executa o programa
if __name__ == "__main__":
    main()