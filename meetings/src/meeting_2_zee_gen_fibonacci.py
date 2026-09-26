"""
# meeting_2_zee_gen_fibonacci

provides multiple methods for generating lists of a given length of fibonacci numbers

### functions

each function will generate a loop via...

- `gen_w_loop`: a loop,
- `gen_w_list_comp`: list comprehensions,
- `gen_list_w_array`: fibonacci matrix identity,
- `gen_array_w_binet`: broadcasting binet's formula
- `gen_list_w_binet`: list comprehensions with binet's formula

"""

import numpy as np

def gen_w_loop(num_vals: int) -> list:
    """
    exercise 1: generates a list of the first num_vals of fibonacci numbers 
        using a loop

    args:
        num_vals (int): the number of fibonacci numbers to generate

    returns:
        fibonacci (list): a list containing the first num_vals fibonacci numbers
    """
    # initialize
    fibonacci = []

    # collect each fibonacci number in the list
    for index in range(num_vals):
        if index <= 1:
            fibonacci.append(index)
        else:
            fibonacci.append(fibonacci[index - 1] + fibonacci[index - 2])

    return fibonacci

def gen_w_list_comp(num_vals: int) -> list:
    """
    exercise 2: generates a list of the first num_vals of fibonacci numbers 
        using list comprehensions
    
    args:
        num_vals (int): the number of fibonacci numbers to generate

    returns:
        fibonacci (list): a list containing the first num_vals fibonacci numbers
    """
    # define count and initialize
    dummy_count, fib = (2 * num_vals), [0, 1]

    # list comp to gen fib number list
    fibonacci = [
        fib.append(fib[index - 1] + fib[index -2]) 
        if index < num_vals 
        else fib[index - num_vals]
        for index in range(2, dummy_count)
    ][num_vals - 2:]
    
    return fibonacci

def gen_list_w_array(num_vals: int) -> list:
    """
    exercise 3: generates a list of the first num_vals of fibonacci numbers 
        using arrays
        
    args:
        num_vals (int): the number of fibonacci numbers to generate

    returns:
        fibonacci (list): a list containing the first num_vals fibonacci numbers 
            [shape (num_vals,)]
    """

    fib_root = np.array([[1, 1], [1, 0]])

    fibonacci = [0, 1]

    for n in range(2, num_vals - 1):
        ((fn_next, fn_curr), _) = np.linalg.matrix_power(fib_root, n)

        fibonacci[n:n+1] = [int(fn_curr), int(fn_next)]

    return fibonacci

def gen_array_w_binet(num_vals: int) -> np.signedinteger:
    """
    exercise 4.a: generates an integer array of the first num_vals of fibonacci 
    numbers using arrays
        
    args:
        num_vals (int): the number of fibonacci numbers to generate

    returns:
        fibonacci (ndarray): an array of signed integers containing the first 
            num_vals fibonacci numbers [shape (1,num_vals)]
    """
    n = np.arange(0, num_vals)

    fibonacci = np.int_(((1 + np.sqrt(5)) ** n - (1 - np.sqrt(5)) ** n) / ((2 ** n) * np.sqrt(5)))

    return fibonacci


def gen_list_w_binet(num_vals : int) -> list:
    """
    exercise 4.b: generates an integer array of the first num_vals of fibonacci 
    numbers using arrays
        
    args:
        num_vals (int): the number of fibonacci numbers to generate

    returns:
        fibonacci (list): a list containing the first num_vals fibonacci numbers 
    """
    phi, psi = (1 + np.sqrt(5)) / 2, (1 - np.sqrt(5)) / 2

    fibonacci = [
        int((phi ** n - psi ** n) / np.sqrt(5))
        for n in range(num_vals)
    ]

    return fibonacci


if __name__ == "__main__":

    num_vals = 50

    print(gen_list_w_binet(num_vals))