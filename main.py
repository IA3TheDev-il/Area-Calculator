import math
import os

from colorama import just_fix_windows_console
from termcolor import colored, cprint


c = 5

def cls():
    os.system("cls" if os.name == "nt" else "clear")

just_fix_windows_console()

if os.name == "nt":
    os.system("title Area Calculator")

cprint(f"[!] Cans Can Cover {c} Meters", "blue")

print()
print()

def paintCalc(height, width, cover):
    result = math.ceil((height * width) / cover)

    cprint(f"[+] Cans Needed : {result}", "green")

h = int(input(colored("[?] Height Of Wall : ", "yellow")))

print()

w = int(input(colored("[?] Width Of Wall : ", "yellow")))

cls()

paintCalc(height = h, width = w, cover = c)

print()
print()
print()

input(colored("[!] Press Enter To Close The Program\n", "blue"))