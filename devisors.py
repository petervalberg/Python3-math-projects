# This program calculates prime factors and divisors of a natural number (integer/whole number)

import math


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def calc_divisors(number):
    divisors = list()
    temp_list = list()
    for i in range(1, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            temp_list.append(i)
    for element in temp_list:
        divisors.append(element)
        temp_number = int(number / element)
        if temp_number not in divisors:
            divisors.append(temp_number)
    divisors.sort()
    print(f' The {len(divisors)} divisors of {number} are: ', divisors)


def start():
    i = 0
    work_number = 0
    copy_work_number = 0
    prime_list = list()
    factor_list = list()
    type_int = False

    print('\n Prime factors and divisors of a natural number')
    print(' ----------------------------------------------\n')
    while type_int is not True:

        work_number = input(' Write a natural number: ')
        copy_work_number = work_number
        try:
            work_number = int(work_number)
            type_int = True

            if work_number == 2:
                prime_list.append(work_number)
            if work_number > 2:
                prime_list.append(2)
            for i in range(3, work_number + 1, 2):
                if is_prime(i) is True:
                    prime_list.append(i)
        except ValueError:
            print(' Write a natural number (i.e. integer/whole number) > 1.')

    if prime_list[-1] == work_number:
        print(f' {work_number} is a prime number.')
    else:
        while work_number > 0:
            for i in prime_list:
                if work_number % i == 0:
                    factor_list.append(i)
                    break
            work_number = work_number // i
        print(f'\n Prime factors for {copy_work_number} are: {factor_list}')
        calc_divisors(int(copy_work_number))


start()