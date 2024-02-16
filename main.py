from flet import Page, TextField, ElevatedButton, Row, ControlEvent
import flet


async def main(page: Page):
    page.title = 'Калькулятор'
    page.window_height = 550
    page.window_width = 350
    page.window_resizable = False

    async def check_input_number(e: ControlEvent):
        if not input_field.value.isalpha():
            if input_field.value == '0':
                input_field.value = e.control.text
            else:
                input_field.value += e.control.text
        else:
            input_field.value = 0
        await page.update_async()

    async def result_sum_string(e: ControlEvent):
        result = eval(input_field.value)
        input_field.value = f'{result}'
        await page.update_async()

    async def remove_last_element(e: ControlEvent):
        """Удаляем последний символ"""
        input_field.value = input_field.value[:-1]
        await page.update_async()

    async def clear_full_string(e: ControlEvent):
        input_field.value = '0'
        await page.update_async()

    input_field = TextField(
        value='0',
        text_align='right',
        color='grey',
        bgcolor='white'
    )
    await page.add_async(input_field)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, '/', '+', '-']
    buttons = []
    for number in numbers:
        button = ElevatedButton(text=f'{number}', width=90, height=40, on_click=check_input_number)
        buttons.append(button)
        if len(buttons) == 3:
            await page.add_async(
                Row(buttons, alignment=flet.MainAxisAlignment.CENTER)
            )
            buttons = []
    else:
        equally = ElevatedButton(text='=', width=90, height=40, on_click=result_sum_string)
        remove_last_element_button = ElevatedButton(text='C', width=90, height=40, on_click=remove_last_element)
        clear_full_string_button = ElevatedButton(text='CE', width=90, height=40, on_click=clear_full_string)
        await page.add_async(
            Row(
                [remove_last_element_button, equally, clear_full_string_button],
                alignment=flet.MainAxisAlignment.CENTER
            ))

    await page.update_async()


if __name__ == '__main__':
    flet.app(target=main)
