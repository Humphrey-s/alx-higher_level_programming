#!/usr/bin/python3

def multiple_returns(sentence):

    char = ()

    n = len(sentence)

    if n == 0:

        return 0, None

    else:

        return n, sentence[0]
