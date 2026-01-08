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
        dpg.add_button(label='Button', callback=on_button_click)
        dpg.add_checkbox(label='Checkbox', callback=on_checkbox_tick)
        dpg.add_slider_int(label='Slider Int', callback=on_slider_changed)
        dpg.add_input_text(label='Input text',callback=on_input_text_change)
        dpg.add_input_text(label='Password', default_value='Your password will appear here', tag='password_field', readonly=True)
        dpg.add_button(label='Copy password', callback=copy_password)
        with dpg.group(horizontal=True):
            dpg.add_text('Status:')
            dpg.add_text('', tag='copy_status')
        dpg.add_button(label='Exit PyPass',callback=lambda sender, app_data: dpg.configure_item('confirm_exit_modal', show=True))