import flet as ft
from flet import *
import time
import threading
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def HomeView(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.DARK 
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_ORANGE)
    page.title = "PROGRAMADORES"
    page.window.width = 500
    page.window.height = 800
    page.window.max_width = 500
    page.window.max_height = 800
    page.window.min_width = 500
    page.window.min_height = 800
    page.scroll = ft.ScrollMode.AUTO

    def mudar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.theme = ft.Theme(color_scheme_seed=ft.Colors.INDIGO)
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_ORANGE)
        print(f"Tema alterado para: {page.theme_mode}")
        page.update()

    def clicou_menu(e):
        item = e.control.text
        if item == "Suporte":
            print("Abrir suporte...")
        elif item == "Configurações":
            print("Abrir configurações...")
        elif item == "Tema":
            mudar_tema(None)

    # ===================================== CRIANDO ELEMENTOS
    appbar = ft.AppBar(
        leading_width=10,
        title=ft.Text("Desempenho", weight="bold"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,  
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="TEMA", icon="WB_SUNNY_OUTLINED", on_click=mudar_tema),
                     ft.PopupMenuItem(text="ACESSIBILIDADE", icon="HEARING", on_click=lambda e: print("Acessibilidade")),
                    ft.PopupMenuItem(text="CONFIGURAÇÕES", icon="SETTINGS_OUTLINED", on_click=clicou_menu),
                    ft.PopupMenuItem(text="SUPORTE", icon="HELP_OUTLINE_ROUNDED", on_click=clicou_menu),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="SAIR", icon="CLOSE_ROUNDED", on_click=clicou_menu),        
                ]
            ),
        ],
    )
     
    def criar_grafico():
        # Dados
        modulos = ['Módulo 1', 'Módulo 2', 'Módulo 3']
        notas = [45, 52, 100]
        frequencias = [38, 45, 50] 

        # Configurações do gráfico
        x = np.arange(len(modulos))
        largura = 0.35

        fig, ax = plt.subplots(figsize=(10, 6))

        # Função para determinar a cor baseada no valor
        def definir_cor(valor):
            if valor >= 75:
                return "#074723"  # Verde
            elif valor >= 50:
                return "#FFD900"  # Amarelo
            else:
                return "#990000"  # Vermelho

        # Criar listas de cores para cada conjunto de barras
        cores_notas = [definir_cor(nota) for nota in notas]
        cores_frequencias = [definir_cor(freq) for freq in frequencias]

        # Criar barras com cores condicionais
        barras1 = ax.bar(x - largura/2, notas, largura, label='Nota (%)', color=cores_notas, alpha=0.8)
        barras2 = ax.bar(x + largura/2, frequencias, largura, label='Frequência (%)', color=cores_frequencias, alpha=0.8)

        # Personalizar o gráfico
        ax.set_title('Desempenho do Aluno', fontsize=18, fontweight='bold', pad=20)
        ax.set_ylabel('Porcentagem (%)', fontsize=18)
        ax.set_xticks(x)
        ax.set_xticklabels(modulos)
        ax.legend(frameon=True, fancybox=True, shadow=True)

        # Adicionar valores nas barras com melhor formatação
        def adicionar_valores(barras):
            for barra in barras:
                altura = barra.get_height()
                ax.text(barra.get_x() + barra.get_width()/2., altura + 1,
                        f'{altura}%', ha='center', va='bottom', fontweight='bold')

        adicionar_valores(barras1)
        adicionar_valores(barras2)

        # Melhorar a estética
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)

        # Ajustar limites do eixo Y para melhor visualização
        ax.set_ylim(0, max(max(notas), max(frequencias)) * 1.15)

        # Adicionar legenda de cores
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#074723', alpha=0.8, label='≥ 75% (Bom)'),
            Patch(facecolor="#FFD900", alpha=0.8, label='50-74% (Regular)'),
            Patch(facecolor="#990000", alpha=0.8, label='< 50% (Crítico)')
        ]
        ax.legend(handles=legend_elements, title='Classificação', loc='upper right', frameon=True, fancybox=True, shadow=True)

        plt.tight_layout()
        
        # Converter gráfico para imagem base64
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        plt.close()
        
        return image_base64

    def criar_analise_texto():
        modulos = ['Módulo 1', 'Módulo 2', 'Módulo 3']
        notas = [45, 52, 100]
        frequencias = [38, 45, 50]
        
        textos = []
        
        for i, modulo in enumerate(modulos):
            # Classificação das notas
            if notas[i] >= 75:
                class_nota = "Bom"
            elif notas[i] >= 50:
                class_nota = "Regular"
            else:
                class_nota = "Crítico"
            
            # Classificação das frequências
            if frequencias[i] >= 75:
                class_freq = "Bom"
            elif frequencias[i] >= 50:
                class_freq = "Regular"
            else:
                class_freq = "Crítico"
            
            situacao = "Aprovado" if notas[i] >= 60 and frequencias[i] >= 75 else "Em recuperação"
            
            textos.append(
                ft.Text(
                    f"{modulo}: Nota {notas[i]}% ({class_nota}), "
                    f"Frequência {frequencias[i]}% ({class_freq}) - {situacao}",
                    size=14,
                    weight=ft.FontWeight.W_500
                )
            )
    
        return ft.Column(textos)

    # Função para mudar de tela conforme índice do NavigationBar
    def mudar_tela(e):
        page.views.clear()
        if e.control.selected_index == 0:
            page.views.append(View(
                route="/home",
                controls=[appbar, grafico_container, analise_container, navbar],
                vertical_alignment="center",
                horizontal_alignment="center"
            ))
        elif e.control.selected_index == 1:
            page.views.append(View(
                route="/desempenho",
                controls=[appbar, grafico_container, analise_container, navbar],
                vertical_alignment="center",
                horizontal_alignment="center"
            ))
        elif e.control.selected_index == 2:
            page.views.append(View(
                route="/notificacoes",
                controls=[appbar, grafico_container, analise_container, navbar],
                vertical_alignment="center",
                horizontal_alignment="center"
            ))
        elif e.control.selected_index == 3:
            page.views.append(View(
                route="/perfil",
                controls=[appbar, grafico_container, analise_container, navbar],
                vertical_alignment="center",
                horizontal_alignment="center"
            ))
        page.update()

    # Configurando o NavigationBar
    navbar = ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Início"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.BAR_CHART_OUTLINED,
                selected_icon=ft.Icons.BAR_CHART,
                label="Desempenho"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                selected_icon=ft.Icons.NOTIFICATIONS,
                label="Notificações"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON_OUTLINED,
                selected_icon=ft.Icons.PERSON,
                label="Perfil"
            ),
        ],
        on_change=mudar_tela
    )

    # Criar containers individuais sem o container principal
    grafico_container = ft.Container(
        content=ft.Image(src_base64=criar_grafico()),
        padding=10,
        margin=10,
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 0)
        )
    )

    analise_container = ft.Container(
        content=criar_analise_texto(),
        padding=15,
        margin=10,
        border_radius=10,
        bgcolor=ft.Colors.BLUE_GREY_50,
    )

    # ====================================================================================
    # Adicionar todos os componentes à página diretamente
    page.add(
        appbar,
        grafico_container,
        analise_container,
        navbar
    )

    return ft.View(
        route="/home",
        controls=[
            appbar,
            grafico_container,
            analise_container,
            navbar
        ],
        vertical_alignment="center",
        horizontal_alignment="center"
    )


ft.app(target=HomeView)