import flet as ft

def main(page: ft.Page):
    page.title = "Troca de Telas - Exemplo"
    
    # Tela 1 - Login
    def tela_login():
        return ft.Column(
            controls=[
                ft.Text("Tela de Login", size=30, weight="bold"),
                ft.TextField(label="Usuário"),
                ft.TextField(label="Senha", password=True),
                ft.ElevatedButton(
                    "Entrar",
                    on_click=lambda _: mudar_tela(tela_principal())
                ),
            ],
            alignment="center",
            horizontal_alignment="center"
        )
    
    # Tela 2 - Principal
    def tela_principal():
        return ft.Column(
            controls=[
                ft.Text("Tela Principal", size=30, weight="bold"),
                ft.Text("Bem-vindo ao app!"),
                ft.ElevatedButton(
                    "Voltar para Login",
                    on_click=lambda _: mudar_tela(tela_login())
                ),
            ],
            alignment="center",
            horizontal_alignment="center"
        )
    
    # Função para trocar telas
    def mudar_tela(nova_tela):
        page.controls.clear()  # Limpa a tela atual
        page.add(nova_tela)    # Adiciona a nova tela
        page.update()          # Atualiza a página
    
    # Inicia com a tela de login
    mudar_tela(tela_login())

ft.app(target=main)