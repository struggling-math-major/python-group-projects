import numpy as np
###############################
# constants
n = 50
###############################
# 1
fib1 = []
# we need to store two numbers for each calculation, so make a two element dummy list
dump = [0,1]
for i in range(n):
    # store the second entry of the dummy list into answer
    fib1.append(dump[-1])
    # update the dummy list
    dump = [dump[1], dump[0] + dump[1]]
print(fib1)
###############################
# 2a
# one liner I made using basically the same ideas as above
print( [(ep:=[1,1])[i] if i < 2 else (ep:=[ep[0]+ep[1],ep[0]])[0] for i in range(n) ] )
# 2b
# one of many methods in the stackExchange, purposely made to not rely on := operator
fib2 = [1,1]
[fib2.append(fib2[-1] + fib2[-2]) for i in range(n-2)]
print(fib2)
###############################
# 3
my_mat = np.array([[1,1],[1,0]])
# 3a
# dummy array
f_mat = my_mat
# this time make an array of zeros, and we will update the i-th spot
fib3a = np.zeros(n,dtype=int)
for i in range(n):
    # similar in construction to (1), but we are re-filling spots in the array
    fib3a[i] = f_mat[1,0]
    f_mat = f_mat @ my_mat
print(fib3a)
# 3b
fib3b = np.zeros(n,dtype=int)
for i in range(n):
    # sometimes we can learn new operations via documentation
    fib3b[i] = np.linalg.matrix_power(my_mat, i+1)[1,0]
print(fib3b)
###############################
# 4
# one liner using the formula and broadcasting and walrus operator I just learned about
print(np.int_(np.floor( ( ( ( 1 + np.sqrt(5)) / (2) ) ** (ns : =np.arange(1,n+1)) - ( ( 1 - np.sqrt(5)) / (2) ) ** ns ) / np.sqrt(5) ))) 


