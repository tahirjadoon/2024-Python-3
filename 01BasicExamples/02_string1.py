import sys

#importing the functions.py and using the methods specified in it
#from functions import printHeader
from functions1_simple import *

#a fucntion that works with different build in string methods
def builtInStringMethods():
    printHeader("builtInStringMethods")
    item = "Some Thing"
    item2 = "hello, and welcome to my world."
    item3 = "Hello, And Welcome To My World!"
    item4 = "banana"
    item5 = "I love apples, apple are my favorite fruit"

    printItemTab(f"Original Item : {item}")
    printItemTab(f".lower() : {item.lower()}")
    printItemTab(f".upper() : {item.upper()}")
    printItemTab(f".find() T : {item.find("T")}", "[index starts from 0 just like C#]")
    printItemTab(f".capitalize() : {item2.capitalize()}", "[Upper case the first letter in this sentence]")
    printItemTab(f".casefold() : {item3.casefold()}", "[Returns a string where all the characters are lower case]")
    printItemTab(f".center() : {item4.center(20)}", "[Print the word \"banana\", taking up the space of 20 characters, with \"banana\" in the middle]")
    printItemTab(f".count() : {item5.count('apple')}", "Return the number of times the value \"apple\" appears in the string")
    printItemTab(f".count(s, start, end) : {item5.count('apple', 10, 24)}", "Return the number of times the value \"apple\" appears in the string")
    
    print()
    printHeader("builtInStringMethods -- format")
    printItemTab("My name is {fname}, I'm {age}".format(fname = "John", age = 36))
    printItemTab("My name is {0}, I'm {1}".format("John",36))
    printItemTab("My name is {}, I'm {}".format("John",36) )
    printItemTab("We have {:<8} chickens.".format(49), "[:<8 Left aligns the result (within the available space)]")
    printItemTab("We have {:>8} chickens.".format(49), "[:> Right aligns the result (within the available space)]")
    printItemTab("We have {:^8} chickens.".format(49), "[:^ Center aligns the result (within the available space)]")
    printItemTab("The temperature is {:=8} degrees celsius.".format(-5), "[:= Places the sign to the left most position)]")
    printItemTab("The temperature is between {:+} and {:+} degrees celsius.".format(-3, 8), "[:+ Use a plus sign to indicate if the result is positive or negative)]")
    printItemTab("The temperature is between {:-} and {:-} degrees celsius.".format(-3, 8), "[:- Use a minus sign for negative values only)]")
    printItemTab("The temperature is between {: } and {: } degrees celsius.".format(-3, 8), "[: Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers))]")
    printItemTab("The universe is {:,} years old.".format(13800000000), "[:, Use a comma as a thousand separator]")
    printItemTab("The universe is {:_} years old.".format(13800000000), "[:_ Use a underscore as a thousand separator]")
    printItemTab("The binary version of {0} is {0:b}".format(5), "[:b binary format]")
    printItemTab("The binary version of {0} is {0:c}".format(5), "[:c converts the value into the corresponding unicode character]")
    printItemTab("We have {:d} chickens.".format(0b101), "[:d decimal format, to convert a number, in this case a binary number, into decimal number format]")
    printItemTab("We have {:e} chickens.".format(5), "[:e Scientific format, with a lower case e]")
    printItemTab("We have {:E} chickens.".format(5), "[:E Scientific format, with a upper case e]")
    printItemTab("The price is {:.2f} dollars.".format(45), "[:f Fix point number format]")
    printItemTab("The price is {:f} dollars.".format(45), "[:f Fix point number format]")
    printItemTab("The octal version of {0} is {0:o}".format(10), "[:o Octal format]")
    printItemTab("The Hexadecimal version of {0} is {0:x}".format(10), "[:x Hex format, lower case]")
    printItemTab("The Hexadecimal version of {0} is {0:X}".format(10), "[:X Hex format, upper case]")
    printItemTab("You scored {:%}".format(0.25), "[:% Percentage format]")
    printItemTab("You scored {:.0%}".format(0.25), "[:% Percentage format]")

    print()
    printHeader("builtInStringMethods -- string functions")
    printItemTab("Other string functions to look at are: ")
    printItemTab(f"{Fore.GREEN}encode(), endswith(), expandtabs(), index(), isalnum(), isalpha(), isascii(), {Style.RESET_ALL}")
    printItemTab(f"{Fore.GREEN}isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), {Style.RESET_ALL}")
    printItemTab(f"{Fore.GREEN}isspace(), istitle(), isupper(), join(), ljust(), lstrip(), maketrans(), {Style.RESET_ALL}")
    printItemTab(f"{Fore.GREEN}partition(), replace(), rfind(), rindex(), rjust(), rpartition(), {Style.RESET_ALL}")
    printItemTab(f"{Fore.GREEN}rsplit(), rstrip(), split(), splitlines(), startswith(), strip(), {Style.RESET_ALL}")
    printItemTab(f"{Fore.GREEN}swapcase(), title(), translate(), zfill() {Style.RESET_ALL}")
    print()
    printFooter()

def main():
   #calling buildInStringMethods
   builtInStringMethods()

if __name__ == '__main__':
  main()