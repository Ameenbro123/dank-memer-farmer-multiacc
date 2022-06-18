from ctypes.wintypes import tagMSG
import time
import random
import os
import requests
from pyautogui import *
import pyautogui
import threading as th
import keyboard
import numpy as np
import win32api, win32con
import sys

tokens = (open("tokens.txt","r).readlines()).strip()
payload1 = {
  'content': "pls fish"
}
payload2 = {
  'content': "pls dig"
}
payload3 = {
  'content': "pls hunt"
}
payload4 = {
  'content': "pls sell"
}
def randtime():
  time.sleep(random.randint(2,4))
i = 0
def click(x,y):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(0.1)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def spam(token):
  header = {
    'authorization': token
  }
  while True:
    time.sleep(random.randint(35,50))
    whichfunc = random.randint(1,4)
    if whichfunc == 1:
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload2,headers=header)
      randtime()
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload1,headers=header)
      randtime()
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload3,headers=header)
    elif whichfunc == 2:
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload3,headers=header)
      randtime()
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload2,headers=header)
      randtime()
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload1,headers=header)
    elif whichfunc == 3:
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload1,headers=header)
      randtime()
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload3,headers=header)
      randtime()
      t = requests.post("https://discord.com/api/v9/channels/987584905678577727/messages",data=payload2,headers=header)
    else:
      pass
for i in tokens:
  (th.Thread(target=spam, args=(i,))).start()
try:
  while True: time.sleep(1)
except KeyboardInterrupt:
  sys.exit("I luv balls.")
