import time
import requests
import os
import random
from pystyle import Colors, Colorate
from time import sleep


mainlink = 'https://gift.truemoney.com/campaign/?v='
number = 'abcdefghijklmnopqrstuvwxyzAljv6ALaOTU7peCUu1Aljv6ALaOTU7peCUu1Aljv6ALaOTU7peCUu1Aljv6ALaOTU7peCUu1'
number2 = 'abcdefghijklmnopqrstuvwxyzAljv6ALaOTU7peCUu1Aljv6ALaOTU7peCUu1Aljv6ALaOTU7peCUu1Aljv6ALaOTU7peCUu1'



def rb(text):
        return (Colorate.Horizontal(Colors.rainbow, '                                 ' + text))


os.system('cls')
print(Colorate.Horizontal(Colors.rainbow, '''

  ______   ________  __    __  ________  _______   __    __  __       __   ______   __        __        ________  ________ 
 /      \ |        \|  \  |  \|        \|       \ |  \  |  \|  \  _  |  \ /      \ |  \      |  \      |        \|        \
|  $$$$$$\| $$$$$$$$| $$\ | $$ \$$$$$$$$| $$$$$$$\| $$  | $$| $$ / \ | $$|  $$$$$$\| $$      | $$      | $$$$$$$$ \$$$$$$$$
| $$ __\$$| $$__    | $$$\| $$   | $$   | $$__| $$| $$  | $$| $$/  $\| $$| $$__| $$| $$      | $$      | $$__       | $$   
| $$|    \| $$  \   | $$$$\ $$   | $$   | $$    $$| $$  | $$| $$  $$$\ $$| $$    $$| $$      | $$      | $$  \      | $$   BY:BFHMSC
| $$ \$$$$| $$$$$   | $$\$$ $$   | $$   | $$$$$$$\| $$  | $$| $$ $$\$$\$$| $$$$$$$$| $$      | $$      | $$$$$      | $$   
| $$__| $$| $$_____ | $$ \$$$$   | $$   | $$  | $$| $$__/ $$| $$$$  \$$$$| $$  | $$| $$_____ | $$_____ | $$_____    | $$   
 \$$    $$| $$     \| $$  \$$$   | $$   | $$  | $$ \$$    $$| $$$    \$$$| $$  | $$| $$     \| $$     \| $$     \   | $$   
  \$$$$$$  \$$$$$$$$ \$$   \$$    \$$    \$$   \$$  \$$$$$$  \$$      \$$ \$$   \$$ \$$$$$$$$ \$$$$$$$$ \$$$$$$$$    \$$   
                                                                                                                           
                                                                                                                           
                                                                                                                           


'''))
print(' ')
print(' ')
print(' ')
print(' ')

webhooklink = input(rb('WEBHOOK LINK > '))
amount = int(input(rb('HOW MUCH WALLET > ')))
input(rb('PRESS ENTER TO START > '))
print(' ')
for i in range(amount):
    message = mainlink + random.choice(number2) + random.choice(number) + random.choice(number) + random.choice(number) + random.choice(number) + random.choice(number) + '/'
    _data = requests.post(webhooklink, json={'content': message}, headers={'Content-Type': 'application/json'})
    if _data.status_code == 204:
        print(rb(f'[+] SEND WALLET {message}'))
    if _data.status_code == 429:
        print(f"[-] rate limited")
        time.sleep(1)