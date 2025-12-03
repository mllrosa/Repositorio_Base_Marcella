import flet as ft
 # page.add(ft.Text(value='AA AA')

def main(page: ft.Page):
    
    def add_task(a):
        print('Novo Texto:', new_task.value)
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value=''
        page.update()

    new_task = ft.TextField(hint_text='Insira uma tarefa...')
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)

    page.add(new_task, new_button)
ft.app(target=main)