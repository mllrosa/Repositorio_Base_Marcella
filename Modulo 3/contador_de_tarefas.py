import flet as ft
 # page.add(ft.Text(value='AA AA')

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = 'Tarefas'
    page.window.width = 350
    page.window.height=550
    page.padding = ft.padding.only(top=20,left=20,right=20,bottom=20)
    
    def add_task(a):
        print('Novo Texto:', new_task.value)
        task_list.controls.append(ft.Checkbox(label=new_task.value))
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value=''
        page.update()

    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)

    task_list = ft.Column()


    card = ft.Column(
        width=400,
            controls=[
                ft.Row(
                    controls=[
                        new_task,
                        new_button
                    ]
                ),
                task_list,
            ]
        )


    page.add(card)
ft.app(target=main)