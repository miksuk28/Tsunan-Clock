from fileinput import filename
import PySimpleGUI as sg
#from output import numbers
from datetime import datetime
from threading import Timer
from random import randint

current_time = datetime.now()
hour, minute = current_time.strftime("%H"), current_time.strftime("%M")
second = current_time.strftime("%S")

layout = [
    [sg.Image(f"assets/{int(hour)}.png", key="-HOUR-", size=(100,200)), sg.Image(f"assets/{int(minute)}.png", key="-MINUTE-", size=(100,200)), sg.Image(f"assets/{int(second)}.png", key="-SECOND-", size=(100,200))],
]

window = sg.Window("TEST", layout=layout, finalize=True, no_titlebar=True, grab_anywhere=True, return_keyboard_events=True)
window.bind("<ESCAPE>", "Exit")

def change_number():
    print("cock")
    window["-HOUR-"].update(filename=f"assets/{randint(0,59)}.png")

def main():
    while True:
        s = Timer(1.0, change_number)
        s.start()
        
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "Escape:27"):
            break
        
        elif event in ("a"):
            window["-HOUR-"].update(filename="assets/1.png")

        print(event, values)

    window.close()


if __name__ == "__main__":
    main()