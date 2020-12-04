import random
import os
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

cards = [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]
random.shuffle(cards)

card_names = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_values = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]

player = []
p_card = []
cpu = []
cpu_card = []

def reset():
  os.system('clear')
  os.execv(sys.executable, ['python'] + sys.argv)


for i in range(0,2):
  num = random.randint(0,13)
  player.append(card_values[num])
  p_card.append(card_names[num])

def cpu_load(cards):
  for i in range(0,cards):
    num = random.randint(0,13)
    cpu.append(card_values[num])
    cpu_card.append(card_names[num])

cpu_load(2)

def print_dealt():
  for i in range(0,len(p_card)):
    x = cards[i]
    if x == 0:
      print(Fore.RED + p_card[i] + "♥  Value:" + str(player[i]) + Style.RESET_ALL)
    elif x == 1:
      print(p_card[i] + "♠  Value:" + str(player[i]))
    elif x == 2:
      print(Fore.RED + p_card[i] + "♦  Value:" + str(player[i]) + Style.RESET_ALL)
    else:
      print(p_card[i] + "♣  Value:" + str(player[i]))

print_dealt()

print("The Dealer's face up card is " + cpu_card[0])

stand = input(Fore.GREEN +"Hit or Stand? (H/S)"+ Style.RESET_ALL)
stand.lower()
while stand == "h":
  player.append(cpu[1])
  p_card.append(cpu_card[1])
  cpu.pop(1)
  cpu_card.pop(1)
  cpu_load(1)
  total = 0
  for i in player:
    total += i
  print("Total: " + str(total))
  print_dealt()
  if total > 21:
    input(Fore.RED +"BUST!"+ Style.RESET_ALL)
    reset()
  stand = input(Fore.GREEN +"Hit or Stand? (H/S)"+ Style.RESET_ALL)
  stand.lower()

total = 0
for i in player:
    total += i
print("Your Total: " + str(total))
time.sleep(2)
cputotal = 0
for i in cpu:
    cputotal += i
print("Dealer's Total: " + str(cputotal))
time.sleep(0.5)
if total > cputotal or cputotal > 21:
  input(Fore.YELLOW +"YOU WIN 🙂 "+ Style.RESET_ALL)
elif total < cputotal and cputotal < 22:
  input(Fore.BLUE +"YOU LOSE 😔 "+ Style.RESET_ALL)
elif total == cputotal:
  input(Fore.GREEN +"YOU... draw? 😐 "+ Style.RESET_ALL)
reset()