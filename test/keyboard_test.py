# import curses
# import os
#
# def main(win):
#     win.nodelay(True)
#     key=""
#     win.clear()
#     win.addstr("Detected key:")
#     while 1:
#         try:
#            key = win.getkey()
#            win.clear()
#            win.addstr("Detected key:")
#            win.addstr(str(key))
#            if key == os.linesep:
#               break
#         except Exception as e:
#            # No input
#            pass
#
# curses.wrapper(main)

import sys, termios, tty, os, time


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


button_delay = 0.1

while True:
    char = getch()

    if (char == "p"):
        print("Stop!")
        exit(0)

    if (char == "a"):
        print("Left pressed")
        time.sleep(button_delay)

    elif (char == "d"):
        print("Right pressed")
        time.sleep(button_delay)

    elif (char == "w"):
        print("Up pressed")
        time.sleep(button_delay)

    elif (char == "s"):
        print("Down pressed")
        time.sleep(button_delay)

    elif (char == "1"):
        print("Number 1 pressed")
        time.sleep(button_delay)