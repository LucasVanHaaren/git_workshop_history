#!/usr/bin/env python3

from sys import argv

def show_help():
	print(f"Usage : {argv[0]} <NAME>")
	print("")
	print("Print a generic greeting, or a personnal one if a name is provided")
	print("")
	print("ARGUMENTS:")
	print("- NAME : (OPTIONNAL) Print a name to greet instead of 'Hello World'")
	print("")

if len(argv) == 1:
    print("Hello World !")
elif len(argv) == 2:
    print(f"Hello {argv[1]}")
else:
    show_help()

