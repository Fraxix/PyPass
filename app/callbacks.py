import dearpygui.dearpygui as dpg
from app.config import ERROR_NO_CHAR_SELECTED,INFO_PASSWORD_COPIED,ERROR_PASSWORD_EMPTY, INFO_PASSWORD_GENERATED
import secrets
import string

def get_characters():
    characters = ""
    if dpg.get_value('include_uppercase'):
        characters += string.ascii_uppercase
    if dpg.get_value('include_lowercase'):
        characters += string.ascii_lowercase
    if dpg.get_value('include_numbers'):
        characters += string.digits
    if dpg.get_value('include_symbols'):
        characters += string.punctuation
    return characters

def generate_password(sender):
    if sender != 'generate_button' and not dpg.get_value('auto_generate_toggle'):
        return
    dpg.set_value('tmp_password_generated_info', '')
    
    characters = get_characters()
    if not characters:
        dpg.set_value('tmp_checkbox_info',ERROR_NO_CHAR_SELECTED)
        dpg.set_value('password_field', '')
        return
    dpg.set_value('tmp_checkbox_info','')
    dpg.set_value('copy_status', '')
    
    length = dpg.get_value('password_length')
    password = ''.join(secrets.choice(characters) for _ in range(length))
    dpg.set_value('password_field', password)
    dpg.set_value('tmp_password_generated_info', INFO_PASSWORD_GENERATED)

    if dpg.get_value('auto_copy_toggle'):
        copy_password()

def toggle_password_visibility():
    dpg.configure_item('password_field', password=not dpg.get_value('show_password'))

def copy_password():
    password = dpg.get_value('password_field')
    if not password:
        dpg.set_value('copy_status', ERROR_PASSWORD_EMPTY)
        return    
    dpg.set_clipboard_text(password)
    dpg.set_value('copy_status', INFO_PASSWORD_COPIED)

def exit_app():
    dpg.stop_dearpygui()

def close_exit_dialog():
    dpg.configure_item('confirm_exit_modal', show=False)