import matplotlib.pyplot as plt
import numpy as np
import textwrap
import pandas as pd
import random
import math
#the code below swill solve any one variable function via genetic algorithm where variable is integer


#Note: if you face " best_solution.append( next_gen_sorted[0]) #store the best solution in each iteration IndexError: list index out of range" error change fitness function value or range of selected first population
#this error occurs due to the fact that there was no good solution in ith iteration
#variable to store the best solution
best_solution = []
#target function
def target(x):
    return math.exp(-x) #goal is to minimize the target function
#generating random answers
solutions = []
bits =8
for i in range(500): #generating random answers(ASSUMPTION: variables are integer and positive)
    solutions.append(bin(random.randint(0, 30))[2:].zfill(bits))  # solution = (np.random.choice(np.arange(0,2),size=bits)) #generating number within the range
    digits = []
def fitness(solution):
    try:
        y = target(solution)
        if (y < 0.000001): #will change based on target function
            return 99999
        else:
            return solutions
    except ZeroDivisionError:
        print('not defined')

length_of_selection = 100 #initial value and will be change in each iteration
def select(solutions): #this funcitons will check the fitness of solutions and sort best answers of given solutions
    overal_score = 0
    next_gen = []
    target_value = []
    next_gen_sorted = []
    counter = 0
    for i in range(len(solutions)):
        if fitness(int(solutions[i],2))==99999:
            next_gen.append(int(solutions[i],2))
            target_value.append(target(int(solutions[i],2)))
            print(f'target value is {target_value}') #getting values of target funciton for each solution
            min_index=(np.argmin(target_value)) #getting index for minimum values
            next_gen_sorted.append(next_gen[min_index])
            counter+=1 #counter to determine numbers of selected good answers
        else:
            print()  
    next_gen_sorted.sort()
    length_of_selection =counter
    next_gen_sorted = next_gen_sorted[:length_of_selection]
    
    best_solution.append( next_gen_sorted[0]) #store the best solution in each iteration

    for i in range(length_of_selection): #determining overal score of each iteration to observe the progress
        overal_score = overal_score+next_gen_sorted[i]
        next_gen_sorted[i] = (bin(int(next_gen_sorted[i]))[2:].zfill(bits))
    print(f'overal score is {overal_score}')     
    return next_gen_sorted


#mutation function
def mutation(gen): #this funcitons change the bits of each selected solution by chance
    mutated = []
    for number in gen:
        for digits in number:
            mutated.append(digits)
        for i in range(len(mutated)):
            if np.random.choice([1,2,3,4]) == 1:
                if mutated[i] == '0':
                    mutated[i] = '1'
                else:
                    mutated[i] = '0'
#concating whole array
    joined = ''.join(map(str, mutated))
#deviding it to even chunks(bits)
    joined = textwrap.wrap(joined, bits)
    
    
    solutions.clear() #clearing previous good answers
    for i in range(len(joined)):
        solutions.append(joined[i]) #adding new values to solution array
    
    return 

for i in range(5): #total number of runs
    mutation(select(solutions))
final_function = {} #to determine the lowest possible answer
for i in best_solution:
    final_function[i]=target(i)
sorted = sorted(final_function.items(), key=lambda kv: kv[1]) #sorting dictionary based on values

print(f'minimum of the funciton is (x value: y value) {sorted}')






