import dearpygui.dearpygui as dpg

def on_button_click(sender):
    print('Button clicked')
    print(f'Sender: {sender}')

def on_checkbox_tick(sender, app_data):
    if app_data:
        print('Checkbox ticked')
        print(f'Sender: {sender}')
    else:
        print('Checkbox unticked')
        print(f'Sender: {sender}')

def on_slider_changed(sender, app_data):
    print(f'Slider value: {app_data}')

def on_input_text_change(sender, app_data):
    print(f'Input text value: {app_data}')

def exit_app(sender, app_data):
    print('Exit PyPass clicked')
    print(f'Sender: {sender}')
    dpg.stop_dearpygui()

def close_exit_dialog(sender, app_data):
    dpg.configure_item('confirm_exit_modal', show=False)