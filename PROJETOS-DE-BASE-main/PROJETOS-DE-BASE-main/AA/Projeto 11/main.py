# 📦 PROJETO 11 — Controle de Estoque
# Monte um sistema de controle de estoque com cadastro de produtos, quantidade e preço.

# Permita atualizar o estoque conforme entradas e saídas.

# 📦 PROJETO 11 — Controle de Estoque

def cadastrar_produto(estoque):
    """Cadastra um novo produto no estoque"""
    print("\n" + "="*50)
    print("📦 CADASTRO DE NOVO PRODUTO")
    print("="*50)
    
    codigo = input("Código do produto: ").strip()
    
    # Verifica se o código já existe
    if codigo in estoque:
        print("❌ Código já existe no estoque!")
        return
    
    nome = input("Nome do produto: ").strip()
    
    try:
        quantidade = int(input("Quantidade inicial: ").strip())
        preco = float(input("Preço unitário R$: ").strip())
    except ValueError:
        print("❌ Quantidade e preço devem ser números válidos!")
        return
    
    if quantidade < 0:
        print("❌ Quantidade não pode ser negativa!")
        return
    
    if preco < 0:
        print("❌ Preço não pode ser negativo!")
        return
    
    estoque[codigo] = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
    
    print(f"✅ Produto '{nome}' cadastrado com sucesso!")

def listar_produtos(estoque):
    """Lista todos os produtos do estoque"""
    if not estoque:
        print("\n📭 Estoque vazio!")
        return
    
    print("\n" + "="*70)
    print("📋 LISTA DE PRODUTOS EM ESTOQUE")
    print("="*70)
    print(f"{'Código':<10} {'Nome':<20} {'Quantidade':<12} {'Preço':<10} {'Valor Total':<12}")
    print("-"*70)
    
    valor_total_estoque = 0
    
    for codigo, produto in estoque.items():
        valor_total = produto['quantidade'] * produto['preco']
        valor_total_estoque += valor_total
        
        print(f"{codigo:<10} {produto['nome']:<20} {produto['quantidade']:<12} "
              f"R$ {produto['preco']:<8.2f} R$ {valor_total:<10.2f}")
    
    print("-"*70)
    print(f"VALOR TOTAL DO ESTOQUE: R$ {valor_total_estoque:.2f}")

def entrada_estoque(estoque):
    """Registra entrada de produtos no estoque"""
    if not estoque:
        print("\n📭 Nenhum produto cadastrado!")
        return
    
    print("\n" + "="*50)
    print("📥 ENTRADA NO ESTOQUE")
    print("="*50)
    
    codigo = input("Código do produto: ").strip()
    
    if codigo not in estoque:
        print("❌ Produto não encontrado!")
        return
    
    produto = estoque[codigo]
    print(f"Produto: {produto['nome']}")
    print(f"Estoque atual: {produto['quantidade']}")
    
    try:
        quantidade_entrada = int(input("Quantidade a adicionar: ").strip())
    except ValueError:
        print("❌ Quantidade deve ser um número inteiro!")
        return
    
    if quantidade_entrada <= 0:
        print("❌ Quantidade deve ser maior que zero!")
        return
    
    produto['quantidade'] += quantidade_entrada
    print(f"✅ Entrada registrada! Novo estoque: {produto['quantidade']}")

def saida_estoque(estoque):
    """Registra saída de produtos do estoque"""
    if not estoque:
        print("\n📭 Nenhum produto cadastrado!")
        return
    
    print("\n" + "="*50)
    print("📤 SAÍDA DO ESTOQUE")
    print("="*50)
    
    codigo = input("Código do produto: ").strip()
    
    if codigo not in estoque:
        print("❌ Produto não encontrado!")
        return
    
    produto = estoque[codigo]
    print(f"Produto: {produto['nome']}")
    print(f"Estoque atual: {produto['quantidade']}")
    
    try:
        quantidade_saida = int(input("Quantidade a retirar: ").strip())
    except ValueError:
        print("❌ Quantidade deve ser um número inteiro!")
        return
    
    if quantidade_saida <= 0:
        print("❌ Quantidade deve ser maior que zero!")
        return
    
    if quantidade_saida > produto['quantidade']:
        print(f"❌ Estoque insuficiente! Disponível: {produto['quantidade']}")
        return
    
    produto['quantidade'] -= quantidade_saida
    print(f"✅ Saída registrada! Novo estoque: {produto['quantidade']}")

def consultar_produto(estoque):
    """Consulta um produto específico"""
    if not estoque:
        print("\n📭 Nenhum produto cadastrado!")
        return
    
    print("\n" + "="*50)
    print("🔍 CONSULTAR PRODUTO")
    print("="*50)
    
    codigo = input("Código do produto: ").strip()
    
    if codigo not in estoque:
        print("❌ Produto não encontrado!")
        return
    
    produto = estoque[codigo]
    valor_total = produto['quantidade'] * produto['preco']
    
    print(f"\n📋 DADOS DO PRODUTO:")
    print(f"Código: {codigo}")
    print(f"Nome: {produto['nome']}")
    print(f"Quantidade em estoque: {produto['quantidade']}")
    print(f"Preço unitário: R$ {produto['preco']:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")

def relatorio_estoque_baixo(estoque, limite=5):
    """Exibe produtos com estoque baixo"""
    produtos_baixo_estoque = {}
    
    for codigo, produto in estoque.items():
        if produto['quantidade'] <= limite:
            produtos_baixo_estoque[codigo] = produto
    
    if not produtos_baixo_estoque:
        print(f"\n✅ Todos os produtos têm estoque acima de {limite} unidades!")
        return
    
    print(f"\n⚠️  PRODUTOS COM ESTOQUE BAIXO (≤ {limite} unidades)")
    print("="*60)
    
    for codigo, produto in produtos_baixo_estoque.items():
        print(f"{codigo} - {produto['nome']}: {produto['quantidade']} unidades")

def main():
    """Função principal do sistema de estoque"""
    estoque = {}
    
    print("🏪 SISTEMA DE CONTROLE DE ESTOQUE")
    print("="*50)
    
    while True:
        print("\n📋 MENU PRINCIPAL")
        print("-"*30)
        print("1. Cadastrar novo produto")
        print("2. Listar todos os produtos")
        print("3. Registrar entrada no estoque")
        print("4. Registrar saída do estoque")
        print("5. Consultar produto")
        print("6. Relatório de estoque baixo")
        print("7. Sair do sistema")
        
        opcao = input("\nEscolha uma opção (1-7): ").strip()
        
        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            entrada_estoque(estoque)
        elif opcao == "4":
            saida_estoque(estoque)
        elif opcao == "5":
            consultar_produto(estoque)
        elif opcao == "6":
            relatorio_estoque_baixo(estoque)
        elif opcao == "7":
            print("\n📊 RESUMO FINAL DO ESTOQUE:")
            valor_total = sum(prod['quantidade'] * prod['preco'] for prod in estoque.values())
            print(f"Total de produtos: {len(estoque)}")
            print(f"Valor total em estoque: R$ {valor_total:.2f}")
            print("👋 Sistema encerrado! Até logo!")
            break
        else:
            print("❌ Opção inválida! Escolha entre 1 e 7.")

# Executa o programa
if __name__ == "__main__":
    main()