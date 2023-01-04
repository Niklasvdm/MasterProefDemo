import math
import matplotlib
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# numbers to binary


# import sys
# print(sys.path)
def bits(b):
    number = b
    toBinary = []
    while (number >= 1):
        toBinary.insert(0, number % 2)
        number = math.floor(number / 2)
    return (toBinary)


def mod_exp(a, b, m):
    noToBinary = bits(b)

    # XS binary algorithm
    XS = ''
    for i in noToBinary:
        if i == 1:
            XS += 'XS'
        else:
            XS += 'S'
    XS = XS[0:-1]
    # uitvoering algoritme
    temp = 1
    for i in XS:
        if i == 'X':
            temp *= a
        else:
            temp = (temp) ** 2
        temp = temp % m
    return temp





def mod_exp_seq(a, b, m):
    seq = [1]
    noToBinary = bits(b)

    # XS binary algorithm
    XS = ''
    for i in noToBinary:
        if i == 1:
            XS += 'XS'
        else:
            XS += 'S'
    XS = XS[0:-1]
    # uitvoering algoritme
    temp = 1
    for i in XS:
        if i == 'X':
            seq = []
            temp *= a % m
        else:
            temp = (temp) ** 2 % m
            seq.append(temp)

    return seq


def find_Inverse(e, m):
    tuple1 = [m, 1, 0]
    tuple2 = [e, 0, 1]

    while (tuple1[0] != 0 and tuple2[0] != 0):
        #print("Tuple 1 is:", tuple1, "Tuple 2 is:" , tuple2)
        if tuple1[0] > tuple2[0]:
            temp = math.floor(tuple1[0] / tuple2[0])
            tuple1[0] = tuple1[0] - temp * tuple2[0]
            tuple1[1] = tuple1[1] - temp * tuple2[1]
            tuple1[2] = tuple1[2] - temp * tuple2[2]
        else:
            temp = math.floor(tuple2[0] / tuple1[0])
            tuple2[0] = tuple2[0] - temp * tuple1[0]
            tuple2[1] = tuple2[1] - temp * tuple1[1]
            tuple2[2] = tuple2[2] - temp * tuple1[2]

    if tuple1[0] > tuple2[0]:
        if tuple1[0] != 1:
            raise Exception(e, 'and', m, 'are NOT coprime')
        return tuple1
    else:
        if tuple2[0] != 1:
            raise Exception(e, 'and', m, 'are NOT coprime')
        return tuple2


# Function to generate n amount of primes
# Alt. : list(filter(is_prime, [i for i in range(2,50)]))
def generate_first_n_primes(n,begin=2):
    some_primes = []
    i : int = begin
    while len(some_primes) != n:
        if is_prime(i):
            some_primes.append(i)
        i += 1
    return some_primes


# Function to return if a number is prime or not
def is_prime(n):
    for i in range(2,math.ceil(n / 2) + 1):
        if (n % i) == 0:
            return False
    return True