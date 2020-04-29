#!/usr/bin/python

import my_pkg.bc as bc
import my_pkg.ui as ui

order='1'

while order != '3':
    order=input("Select menu: 1)conversion 2)union/intersection 3)exit ? ")

    if order=='1':
        x = int(input("input binary number : "), 2)

        print("=> OCT>", bc.btoo(x))
        print("=> DEC>", bc.btod(x))
        print("=> HEX>", bc.btox(x))

    elif order=='2':
        list_1 = input("1st list: ").replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
        list_2 = input("2nd list: ").replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
        print("=> union", ui.union(list_1, list_2))
        print("=> intersection", ui.intersection(list_1, list_2))

    else:
        print("exit the program...")
        break
