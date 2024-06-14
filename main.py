import mouse , pyfiglet , colorama
from colorama import Fore
a = pyfiglet.figlet_format("EZCLICKER") 
print(Fore.MAGENTA + a)
print(Fore.RED + "made by saksham sharma/violent codes")
b = int(input(Fore.MAGENTA + "enter range:"))
for i in range(b):
    mouse.click('left')

