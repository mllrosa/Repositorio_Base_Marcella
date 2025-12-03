# 🔐 PROJETO 10 — Sistema de Login CSV (Versão Simples)
import csv
import os

def carregar_usuarios(arquivo="usuarios_simples.csv"):
    usuarios = {}
    if os.path.exists(arquivo):
        with open(arquivo, 'r', newline='') as f:
            reader = csv.reader(f)
            for linha in reader:
                if len(linha) >= 2:
                    usuarios[linha[0]] = linha[1]
    return usuarios

def salvar_usuarios(usuarios, arquivo="usuarios_simples.csv"):
    with open(arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        for usuario, senha in usuarios.items():
            writer.writerow([usuario, senha])

def cadastrar():
    print("\n--- CADASTRO ---")
    usuario = input("Usuário: ")
    
    usuarios = carregar_usuarios()
    
    if usuario in usuarios:
        print("Usuário já existe!")
        return
    
    senha = input("Senha: ")
    usuarios[usuario] = senha
    salvar_usuarios(usuarios)
    print("Cadastro realizado!")

def login():
    print("\n--- LOGIN ---")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    usuarios = carregar_usuarios()
    
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado!")
        return True
    else:
        print("Usuário ou senha incorretos!")
        return False

def main():
    while True:
        print("\n1. Cadastrar")
        print("2. Login")
        print("3. Ver usuários")
        print("4. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            usuarios = carregar_usuarios()
            print("\n--- USUÁRIOS ---")
            for usuario in usuarios:
                print(f"👤 {usuario}")
        elif opcao == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")

main()