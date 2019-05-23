import random


def learn(x, y, t, w1, w2, b):
    w1 = w1
    w2 = w2
    b = b
    temp = True
    while temp:
        a = w1 * x + w2 * y + b
        if a > 0:
            y = 1
        else:
            y = 0
        e = t - y
        if e != 0:
            w1 = w1 + (e * x) + (e * y)
            w2 = w2 + (e * x) + (e * y)
            b = b + e
        else:
            temp = False
    return a, b, w1, w2
