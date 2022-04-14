#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: April 2022
# This program takes three integers
#   and tells you the greatest one


def main():
    # this function creates the three inputs

    # input
    integer1 = int(input("Enter your first integer: "))
    integer2 = int(input("\nEnter your second integer: "))
    integer3 = int(input("\nEnter your third integer: "))

    # process & output
    if integer1 > integer2 and integer3:
        print("\nThe greatest integer was {}".format(integer1))
    elif integer2 > integer1 and integer3:
        print("\nThe greatest integer was {}".format(integer2))
    elif integer3 > integer1 and integer2:
        print("\nThe greatest integer was {}".format(integer3))
    else:
        print("\nThere is no greater integer.")


if __name__ == "__main__":
    main()
