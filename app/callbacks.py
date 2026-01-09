import dearpygui.dearpygui as dpg
from app.config import ERROR_NO_CHAR_SELECTED,INFO_PASSWORD_COPIED,ERROR_PASSWORD_EMPTY
import random
import string

def generate_password():
    include_uppercase = dpg.get_value('include_uppercase')
    include_lowercase = dpg.get_value('include_lowercase')
    include_numbers   = dpg.get_value('include_numbers')
    include_symbols   = dpg.get_value('include_symbols')

    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    dpg.set_value('tmp_checkbox_info','')

    if not characters:
        dpg.set_value('tmp_checkbox_info',ERROR_NO_CHAR_SELECTED)
        dpg.set_value('password_field', '')
        return
    
    length = dpg.get_value('password_length')
    password = ''.join(random.choice(characters) for _ in range(length))
    dpg.set_value("password_field", password)

def toggle_password_visibility(sender, app_data):
    dpg.configure_item('password_field', password=not dpg.get_value('show_password'))

def copy_password(sender, app_data):
    password = dpg.get_value('password_field')
    if not password:
        dpg.set_value('copy_status', ERROR_PASSWORD_EMPTY)
        return    
    dpg.set_clipboard_text(password)
    dpg.set_value('copy_status', INFO_PASSWORD_COPIED)

def exit_app(sender, app_data):
    print('Exit PyPass clicked')
    print(f'Sender: {sender}')
    dpg.stop_dearpygui()

def close_exit_dialog(sender, app_data):
    dpg.configure_item('confirm_exit_modal', show=False)