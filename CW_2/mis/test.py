import pandas as pd


def my_sum(*arg):
    re = 0
    for x in arg:
        re += x
    return re


d = my_sum(4,3,4,5,6)
print(d)
print("Hellow World")