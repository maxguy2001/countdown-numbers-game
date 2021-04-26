import numpy as np
import itertools

def choose_nums(big, small):
    big_nums = [100, 75, 50, 25]
    numbers = []
    for i in range(big):
        temp_num = np.random.randint(0, 3)
        numbers.append(big_nums[temp_num])
    for i in range(small):
        temp_num = np.random.randint(1, 10)
        numbers.append(temp_num)

    return numbers

def operation_orders(iterations):
    """
    This function returns the order of the 5 operations taken between the 6 numbers to get the target number.
    Each integer corresponds to a basic algabraic operation as such:
    0-add
    1-subtract
    2-multiply
    3-divide
    """
    ops = [0, 1, 2, 3]
    opord = list(itertools.product(ops, ops, ops, ops, ops))
    opord_inst = opord[iterations]

    return opord_inst

def solve(numbers, target):
    all_combinations = list(itertools.permutations(numbers))
#    possible_iterations = np.math.factorial(len(numbers)) * 4**(len(numbers) - 1)
    i = 0
    while i < len(all_combinations):
        combination = list(all_combinations[i])




    return True



