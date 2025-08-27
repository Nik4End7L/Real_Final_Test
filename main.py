import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = 'Список покупок'
    page.theme_mode = ft.ThemeMode.LIGHT
    goods_list = ft.Column()

    filter_type = "all"

    def load_goods():
        goods_list.controls.clear()
        for goods_id, goods_text, completed in main_db.get_goods(filter_type):
            goods_list.controls.append(create_goods_row(goods_id, goods_text, completed))
        page.update()

    def create_goods_row(goods_id, goods_text, completed):
        goods_field = ft.TextField(
            value=goods_text,
            expand=True,
            read_only=True
        )

        goods_checkbox = ft.Checkbox(
            value=bool(completed),
            on_change=lambda e: toggle_goods(goods_id, e.control.value)
        )

        def delete_goods(_):
            main_db.delete_goods(goods_id)
            load_goods()

        delete_button = ft.IconButton(icon=ft.Icons.DELETE, tooltip='Удалить', on_click=delete_goods)

        return ft.Row([
            goods_checkbox,
            goods_field,
            delete_button
        ])

    warning_text = ft.Text(value="",)

    def add_goods(_):
        if goods_input.value:
            main_db.add_goods(goods_input.value)
            load_goods()
            goods_input.value = ''
            warning_text.value = ""
            page.update()

    def toggle_goods(goods_id, is_completed):
        main_db.update_goods(goods_id, completed=int(is_completed))
        load_goods()

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_goods()

    goods_input = ft.TextField(label='Введите товар', expand=True)  # max_length убран
    add_button = ft.ElevatedButton('Добавить', on_click=add_goods)

    filter_buttons = ft.Row(controls=[
        ft.ElevatedButton("Все", on_click=lambda e: set_filter('all')),
        ft.ElevatedButton("Купленное", on_click=lambda e: set_filter('completed')),
        ft.ElevatedButton("Некупленное", on_click=lambda e: set_filter('uncompleted'))
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(ft.Column([
        ft.Row([goods_input, add_button]),
        warning_text,
        filter_buttons,
        goods_list
    ]))

    load_goods()


if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)

