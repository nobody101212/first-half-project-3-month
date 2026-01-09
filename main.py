import flet as ft


def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    
    
    text_hello = ft.Text('Hello world')
    
    def text_name():
        # print(name_input.value)
        name = name_input.value.strip()

        if name:
            text_hello.color = None
            text_hello.value = f'Hello {name}'
            name_input.value = None
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

    
         
    elevated_button = ft.ElevatedButton('send', on_click=text_name)
    

    name_input = ft.TextField(label='Введите что-нибудь')
     
   

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7) 
    
    page.add(text_hello,  name_input, elevated_button, thememode_button)

    
ft.app(target=main)
