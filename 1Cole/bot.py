# -*- coding: utf-8 -*-
import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+573003380663')

sleep(10)

with open ('song.txt','r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")

