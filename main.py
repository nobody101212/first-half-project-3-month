import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Мое первое приложение'

    text_hello = ft.Text('Hello world')

    name_input = ft.TextField(label='Введите что-нибудь')

    def text_name(e):
        name = name_input.value.strip()

        if name:
            now = datetime.now()
            time_str = now.strftime("%Y:%m:%d - %H:%M:%S")

            text_hello.color = None
            text_hello.value = f'Hello {name}\n{time_str}'
            name_input.value = ""
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

        page.update()

    elevated_button = ft.ElevatedButton('send', on_click=text_name)


    page.add( text_hello,name_input,elevated_button)


ft.app(target=main)
