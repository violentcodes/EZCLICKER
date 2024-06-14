import mouse , pyfiglet , colorama
from colorama import Fore
a = pyfiglet.figlet_format("EZCLICKER") 
print(Fore.MAGENTA + a)
b = int(input("enter range:"))
for i in range(b):
    mouse.click('left')

