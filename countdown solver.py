import numpy as np
from itertools import product
from itertools import permutations

def choose_nums(big, small):
    """
    This function takes 2 inputs (number of big number and number of small
    numbers) and returns a list of appropriate randomized inetegers
    """
    #test inputs
    assert type(big) is int, "Function input (big) must be type integer"
    assert type(small) is int, "Function input (small) must be type integer"
    assert big > 0 and big < 6, "Function input (big) must be between 0 and 6"
    assert small > 0 and small < 6, "Function input (small) must be between 0 and 6"
    assert big + small == 6, "Function inputs must sum to 6"

    #create random list
    big_nums = [100, 75, 50, 25]
    numbers = []
    for i in range(big):
        temp_num = np.random.randint(0, 3)
        numbers.append(big_nums[temp_num])
    for i in range(small):
        temp_num = np.random.randint(1, 10)
        numbers.append(temp_num)

    return numbers


def solve(numbers, target):
    """
    Function takes in a list of 6 numbers and a target number then
    evaluates every possible permutation of numbers and operations, returning
    the first sequence of operators and numbers which equal target number
    """

    #test inputs
    assert type(numbers) == list, "Input (numbers) must be a list"
    assert len(numbers) == 6, "Input (numbers) must have length 6"
    assert target > 0 and target < 1000, "target value must between 0 and 1000"

    #make list of permutations of numbers and operators
    all_combinations = list(permutations(numbers))
    operators = ['+', '*', '-', '/']
    all_order_permutations = list(product(operators, repeat = 5))

    #iterate through all possible combinations of numbers and operators
    for i in range(len(all_combinations)):
        for j in range(len(all_order_permutations)):
            operator_combinations = [str(all_combinations[i][0]),
                                     all_order_permutations[j][0],
                                     str(all_combinations[i][1]),
                                     all_order_permutations[j][1],
                                     str(all_combinations[i][2]),
                                     all_order_permutations[j][2],
                                     str(all_combinations[i][3]),
                                     all_order_permutations[j][3],
                                     str(all_combinations[i][4]),
                                     all_order_permutations[j][4],
                                     str(all_combinations[i][5])]

            #turn each combination list into a single string
            formula = ""
            for substring in operator_combinations:
                formula += substring

            #evaluate formula sting and compare to target
            if eval(formula) == target:
                return formula
            else:
                print(eval(formula))

        #check if no solution will be reached
        if i == len(all_combinations):
            return print("No solutions found")

#function generates random target number
def target_number():
    return np.random.randint(100, 999)


def main():
    """
    Main function allows user to choose between manual input and random input.
    Function then returns list of numbers and target. Solution is then revealed
    when requested.
    """

    #user chooses game type
    chs_or_rand = str(input("Would you like to choose numbers or take random ones? \n (type choose or random)"))

    #case if user inputs list manually
    if chs_or_rand == "choose":
        numbers = []
        for i in range(6):
            x = int(input("Input number:"))
            numbers.append(x)
        target = int(input("Input target number (100-999):"))
        print(f"Your numbers are: {numbers}. \n The target number is {target}")
        print("When you are ready to get solutions, enter y")
        cont = str(input())
        if cont == "y":
            print(f"A possible solution is : {solve(numbers, target)}")
        else:
            True

    #case if user chooses random game
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

    #error statement if input does not match options
    else:
        print("Incorrect input. Please try again.")

main()


#failed previous ideas/attempts
"""

def attempt_1(numbers, target):
    all_combinations = list(permutations(numbers))
#    possible_iterations = np.math.factorial(len(numbers)) * 4**(len(numbers) - 1)
    operators = ['+', '*', '-', '/']  # change '//' to '/' for floating point division
    for i in range(len(all_combinations)):
        for opers in product(operators, repeat=len(all_combinations[i]) - 1):
            formula = [str(all_combinations[i][0])]
            for op, operand in zip(opers, all_combinations[i][1:]):
                formula.extend([op, str(operand)])
            formula = ' '.join(formula)
        ##    print('{} = {}'.format(formula, eval(formula)))
            if eval(formula) == target:
                return formula
            else:
                return "No solution found"

def attempt_2(numbers, target):
    all_combinations = list(permutations(numbers))
    operators = ['+', '*', '-', '/']
    all_order_permutations = list(product(operators, repeat=5))
    for opers in product(operators, repeat=5):
        formula = [str(all_combinations[0])]
        for op, operand in zip(opers, all_combinations[1:]):
            formula.extend([op, str(operand)])
        formula = ' '.join(formula)
        if eval(formula) == target:
            return formula
     
def operation_orders(iterations):

 #   (This was an idea for keeping a running list of orders before i landed on eval function)   
 #   This function returns the order of the 5 operations taken between the 6 numbers to get the target number.
 #   Each integer corresponds to a basic algabraic operation as such:
 #   0-add
 #   1-subtract
 #   2-multiply
 #   3-divide
    
    ops = [0, 1, 2, 3]
    opord = list(product(ops, ops, ops, ops, ops))
    opord_inst = opord[iterations]

    return opord_inst       
"""

