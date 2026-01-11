import dearpygui.dearpygui as dpg
from app.callbacks import *

def create_default_theme():
    with dpg.theme() as default_theme:
       with dpg.theme_component(dpg.mvAll):
           dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)
       return default_theme

def create_default_font():
    with dpg.font_registry():
        default_font = dpg.add_font('Fonts/Inter.ttf', 17)
    return default_font

def render_confirm_exit_modal():
    with dpg.window(label='Exit app', modal=True, show=False, no_close=True, tag='confirm_exit_modal'):
        dpg.add_text('Are you sure?')
        with dpg.group(horizontal=True):
            dpg.add_button(label='Yes', callback=exit_app)
            dpg.add_button(label='Cancel',callback=close_exit_dialog)

def render_main_window():
    with dpg.window(tag='main_window', no_title_bar=True, no_collapse=True, no_scroll_with_mouse=True, no_scrollbar=True, no_resize=True):
        with dpg.group(horizontal=True):
            dpg.add_input_text(label='', default_value='Your password will appear here', tag='password_field', readonly=True, password=True)
            dpg.add_checkbox(label='Show Password', callback=toggle_password_visibility, tag='show_password')
        dpg.add_text('', tag='tmp_password_generated_info')

        dpg.add_slider_int(label='Length', tag='password_length', default_value=12, min_value=6, max_value=32, callback=generate_password)
        dpg.add_checkbox(label='Auto Generate Password', callback=generate_password, tag='auto_generate_toggle')
        dpg.add_checkbox(label='Auto Copy Password', callback=generate_password, tag='auto_copy_toggle')

        with dpg.group(horizontal=True):
            dpg.add_checkbox(label='Uppercase', default_value=True, tag='include_uppercase', callback=generate_password)
            dpg.add_checkbox(label='Lowercase', default_value=True, tag='include_lowercase', callback=generate_password)
            dpg.add_checkbox(label='Numbers', default_value=True, tag='include_numbers',callback=generate_password)
            dpg.add_checkbox(label='Symbols', default_value=True, tag='include_symbols', callback=generate_password)
        
        dpg.add_text('', tag='tmp_checkbox_info')

        dpg.add_button(label='Generate Password', callback=generate_password, tag='generate_button')
        dpg.add_button(label='Copy password', callback=copy_password)

        with dpg.group(horizontal=True):
            dpg.add_text('Status:')
            dpg.add_text('', tag='copy_status')

        dpg.add_button(label='Exit PyPass',callback=lambda sender, app_data: dpg.configure_item('confirm_exit_modal', show=True))