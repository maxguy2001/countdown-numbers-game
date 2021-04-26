import numpy as np

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

def solve(numbers):


