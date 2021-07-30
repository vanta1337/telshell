import telnetlib
import time
import os
from threading import Thread
from colorama import Fore, Style
import re

#setting up console
os.system('mode con: cols=55 lines=20')
os.system('title [telshell] by vanta')

#menu
def menu():
    print(Fore.LIGHTBLUE_EX + """

                ┌┬┐┌─┐┬  ┌─┐┬ ┬┌─┐┬  ┬  """ + Fore.LIGHTBLACK_EX + """
                 │ ├┤ │  └─┐├─┤├┤ │  │  """ + Fore.WHITE + """
                 ┴ └─┘┴─┘└─┘┴ ┴└─┘┴─┘┴─┘
                 
                 """)
print(Style.RESET_ALL)
menu()


#setting host and port
host = input("$ host: ")
port = input("$ port: ")

HOST = host
PORT = port

#starting telnet
tn = telnetlib.Telnet(HOST, PORT)
os.system("cls")

#connecting and getting steam name
print("Connecting...")
tn.write(f"name\n".encode('utf-8'))
time.sleep(5)
rawoutpt = tn.read_very_eager().decode('utf-8')
name = re.match(r'"name" = "(.*?)"', rawoutpt).group(1)
os.system("cls")

###custom commands###
def spam():
    i = 0
    istr = str(i)
    while True:
        istr = str(i)
        tn.write(f"say {istr}\n".encode('utf-8'))
        i += 1
        time.sleep(1)

def rainbowui():
    delay = 0.01
    while True:
        tn.write("cl_hud_color 1\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 2\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 3\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 4\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 5\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 6\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 7\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 8\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 9\n".encode('utf-8'))
        time.sleep(delay)
        tn.write("cl_hud_color 10\n".encode('utf-8'))
        time.sleep(delay)

def rainbowxhair():
    delay = 0.01
    index = 0
    while True:
        r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(index/360,1,1))
        tn.write("cl_crosshaircolor_r {}\n".format(r).encode('utf-8'))
        tn.write("cl_crosshaircolor_g {}\n".format(g).encode('utf-8'))
        tn.write("cl_crosshaircolor_b {}\n".format(b).encode('utf-8'))
        index += 1
        if index == 360:
            index = 0
        time.sleep(delay)

def dos():
    while True:
        tn.write(f"echo dos by vanta <3\n".encode('utf-8'))
        
###custom commands###

#main console
menu()
while True:
    cmd = input(f"{name}@" + host + "$>")
    if cmd == "help":
        print("""
        $ help:
        
        help - shows this prompt
        spam - spams numbers with clients name
        rainbowui - makes the hud switch colors
        rainbowxhair - makes crosshair rainbow
        dos - denial of service (lags out client)
        clear - clears shell
        """)
    if cmd == "clear":
        os.system("cls")
        menu()
    if cmd == "spam":
        spamthread = Thread(target = spam)
        spamthread.start()
    if cmd == "rainbowui":
        rainbowuithread = Thread(target=rainbowui)
        rainbowuithread.start()
    if cmd == "rainbowxhair":
        rainbowxhairthread = Thread(target=rainbowxhair)
        rainbowxhairthread.start()
    if cmd == "dos":
        dosthread = Thread(target=dos)
        dosthread.start()
    else:
        tn.write(f"{cmd}\n".encode('utf-8'))
    time.sleep(0.05)
