import numpy as np
from itertools import product
from itertools import permutations

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
    opord = list(product(ops, ops, ops, ops, ops))
    opord_inst = opord[iterations]

    return opord_inst

def solve(numbers, target):
    all_combinations = list(permutations(numbers))
#    possible_iterations = np.math.factorial(len(numbers)) * 4**(len(numbers) - 1)
    operands = numbers
    operators = ['+', '*', '-', '//']  # change '//' to '/' for floating point division
    for opers in product(operators, repeat=len(operands) - 1):
        formula = [str(operands[0])]
        for op, operand in zip(opers, operands[1:]):
            formula.extend([op, str(operand)])
        formula = ' '.join(formula)
    ##    print('{} = {}'.format(formula, eval(formula)))
        if eval(formula) == target:
            return formula
        else:
            return "No solution found"

def target_number():
    return np.random.randint(100, 999)

def main():
    chs_or_rand = str(input("Would you like to choose numbers or take random ones? \n (type choose or random)"))
    if chs_or_rand == "choose":
        numbers = []
        for i in range(6):
            x = int(input("Input number:"))
            numbers.append(x)
        target = target_number()
        print(f"Your numbers are: {numbers}. \n The target number is {target}")
        print("When you are ready to get solutions, enter y")
        cont = str(input())
        if cont == "y":
            print(f"A possible solution is : {solve(numbers, target)}")
        else:
            True

    elif chs_or_rand == "random":
        big = int(input("How many large numbers would you like?"))
        small = 6 - big
        numbers = choose_nums(big, small)
        target = target_number()
        print(f"Your numbers are: {numbers}. \n The target number is {target}")
        print("When you are ready to get solutions, enter y")
        cont = str(input())
        if cont == "y":
            print(f"A possible solution is : {solve(numbers, target)}")
        else:
            True

main()



