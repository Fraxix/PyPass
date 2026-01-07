import dearpygui.dearpygui as dpg
from app.config import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT
from app.ui import create_default_theme, create_default_font, render_main_window, render_confirm_exit_modal

def main():
    dpg.create_context()
    dpg.create_viewport(title=WINDOW_TITLE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    theme = create_default_theme()
    font = create_default_font()

    render_confirm_exit_modal()
    render_main_window()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.bind_theme(theme)
    dpg.bind_font(font)
    dpg.set_primary_window('main_window', True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == '__main__':
    main()
