# Keylogger
A keylogger program which logs all the keys you press untill the program is manually closed from the task manager.
To run the program simply run the code and it starts running the background. When you want to stop the logger, open task manager, search for python and 'end task' the program.

The logger interprets the keys pressed from numpad as a keycode for eg
If you press 9 on the numpad, it gets interpreted as key code 105 (VK_NUMPAD9).
If you press 9 from the top row of the keyboard, it should log it correctly as '9'.
