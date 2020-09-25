"""
Binomial Distribution Calculator.
---------------------------------
n is the number of times the experiment is performed.
p is the probability of success in decimal.
k is the target number of successes.
"""
from math import factorial

combinations = 0


def binomial_coefficient(n, k):
    globals()['combinations'] = (factorial(n)) / (factorial(k) * factorial(n-k))


def equal_to(p, n, k):
    binomial_coefficient(n, k)
    result = combinations * (p**k) * (1-p) ** (n-k)
    print(f"P(X={k}) = {round(result, decimals)}")


def greater(p, n, k):
    result = 0
    for i in range(k+1, n+1):
        binomial_coefficient(n, i)
        result += combinations * (p**i) * (1-p) ** (n-i)
    print("P(X" + u'\u003E' + f"{k}) = {round(result, decimals)}")


def greater_equal(p, n, k):
    result = 0
    for i in range(k, n+1):
        binomial_coefficient(n, i)
        result += combinations * (p**i) * (1-p) ** (n-i)
    print("P(X" + u'\u2265' + f"{k}) = {round(result, decimals)}")


def less(p, n, k):
    result = 0
    for i in range(k-1, -1, -1):
        binomial_coefficient(n, i)
        result += combinations * (p**i) * (1-p) ** (n-i)
    print("P(X" + u'\u003C' + f"{k}) = {round(result, decimals)}")


def less_equal(p, n, k):
    result = 0
    for i in range(k, -1, -1):
        binomial_coefficient(n, i)
        result += combinations * (p**i) * (1-p) ** (n-i)
    print("P(X" + u'\u2264' + f"{k}) = {round(result, decimals)}")


print('---------------------------------------------------------------')
print('The program will compute Binomial and Cumulative Probabilities.')
print('---------------------------------------------------------------\n')
n = int(input('Number of times the experiment is performed: '))
k = int(input('Number of successes: '))
p = float(input('Probability of success (in decimal): '))
decimals = int(input('How may decimals in results: '))
print('')
equal_to(p, n, k)
less(p, n, k)
less_equal(p, n, k)
greater(p, n, k)
greater_equal(p, n, k)

