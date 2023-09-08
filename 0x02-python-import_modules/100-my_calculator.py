#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

def main():

    ln = len(sys.argv)

    if ln == 1 or ln == 2 or ln == 3 or ln > 4:
        print("0".format())
    else:
        op = str(sys.argv[2])
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        match op:
            case "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            case "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            case "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            case "/":
                print("{} / {} = {}".format(a, b, div(a, b)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /".format())

if __name__ == "__main__":
    main()
