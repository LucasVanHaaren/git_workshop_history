#!/usr/bin/env python3

from sys import argv, exit

def show_help():
	print(f"Usage : {argv[0]} <NAME>")
	print("")
	print("Print a generic greeting, or a personnal one if a name is provided")
	print("")
	print("ARGUMENTS:")
	print("- NAME : (OPTIONNAL) Print a name to greet instead of 'Hello World'")
	print("")


def main() -> int:
	if len(argv) == 1:
		print("Hello World !")
		return 0
	elif len(argv) == 2:
		print(f"Hello {argv[1]} !")
		return 0
	else:
		print("Error : Too many arguments")
		show_help()
		return 1

if __name__ == '__main__':
    exit(main())

