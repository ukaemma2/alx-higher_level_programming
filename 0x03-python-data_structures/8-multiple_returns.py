#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is not None:
        lent = len(sentence)
        if lent == 0:
            return (lent, None)
        return (lent, sentence[0])
