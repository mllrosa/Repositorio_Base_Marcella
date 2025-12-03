# 📱 PROJETO 14 — Lista de Afazeres (Versão Simples)
import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.padding = 20
    page.window.width = 400
    page.window.height = 600
    
    tarefas = []
    lista_tarefas = ft.Column()
    
    campo_tarefa = ft.TextField(
        label="Nova tarefa...",
        expand=True
    )
    
    def adicionar_tarefa(e):
        if campo_tarefa.value.strip():
            tarefa = {
                "texto": campo_tarefa.value,
                "concluida": False
            }
            tarefas.append(tarefa)
            campo_tarefa.value = ""
            atualizar_lista()
    
    def alternar_tarefa(index):
        tarefas[index]["concluida"] = not tarefas[index]["concluida"]
        atualizar_lista()
    
    def excluir_tarefa(index):
        tarefas.pop(index)
        atualizar_lista()
    
    def atualizar_lista():
        lista_tarefas.controls.clear()
        
        for i, tarefa in enumerate(tarefas):
            cor = ft.Colors.GREEN if tarefa["concluida"] else ft.Colors.BLACK
            texto = ft.Text(
                tarefa["texto"], 
                color=cor,
                size=16
            )
            
            item = ft.Row([
                ft.Checkbox(
                    value=tarefa["concluida"],
                    on_change=lambda e, idx=i: alternar_tarefa(idx)
                ),
                texto,
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    on_click=lambda e, idx=i: excluir_tarefa(idx)
                )
            ])
            
            lista_tarefas.controls.append(item)
        
        page.update()
    
    page.add(
        ft.Text("✅ Minha Lista", size=24, weight=ft.FontWeight.BOLD),
        ft.Row([
            campo_tarefa,
            ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)
        ]),
        lista_tarefas
    )

ft.app(target=main)
