import sys
from colorama import Fore, Back, Style
#https://pypi.org/project/colorama/ 

"""
Print header
"""
def printHeader(header):
    length = len(header)
    dashes = "-" * length
    print(f"{Fore.YELLOW}{dashes}")
    print(header)
    print(f"{dashes}{Style.RESET_ALL}")

"""
Print footer
"""
def printFooter():
    footer = "^" * 100
    print(f"{Fore.YELLOW}{footer}{Style.RESET_ALL}")
    print()

"""
Print item with tab
"""
def printItemTab(item, help=""):
    tab = "\t"
    if not help:
        print(f"{tab}{item}")
    else:
        print(f"{tab}{item} {Fore.LIGHTYELLOW_EX}{help}{Style.RESET_ALL}")

"""
Print print item no tab
"""
def printItem(item, help):
    if not help:
        print(item)
    else:
        print(f"{item} {Fore.LIGHTYELLOW_EX}{help}{Style.RESET_ALL}")