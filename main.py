#!/usr/bin/env python3

from sys import argv

if len(argv) == 1:
    print("Hello World !")
elif len(argv) == 2:
    print(f"Hello {argv[1]}")
else:
    print("error")

