import os 
import re

def rearrange_equation(equation):
    # print(equation)
    match = re.match(r'(\d+)\s*([\+\-\*/])\s*(\d+)\s*=\s*(\d+)', equation)
    
    if match:
        operand1, operator, operand2, result = match.groups()

        if operator in ('+', '*'):
            sorted_operands = sorted([int(operand1), int(operand2)])
            rearranged_equation = f'{sorted_operands[0]} {operator} {sorted_operands[1]} = {result}'
            return rearranged_equation
        else:
            return equation
    else:
        return equation


lost_game_indices = [902, 906, 912, 914, 919, 921, 928, 930, 931, 932, 933, 936, 938, 948, 949, 950, 951, 957, 961, 968, 969, 972, 975, 979, 982, 984, 986, 988, 989, 991, 992]
booleans = {}

for i in lost_game_indices:
    filename_incorrect = "./info/step_0s/step_0_" + str(i) + ".txt"
    filename_solution = "./solution_steps/prompt_" + str(i) + "_solution_steps.txt"
    equations_incorrect = []
    equations_solution = []
    print(filename_incorrect)
    with open(filename_incorrect, 'r') as f:
        equations_incorrect = f.read().split("\n")
        f.close()
    with open(filename_solution, 'r') as f:
        solutions = f.read().split("***")
        for solution in solutions:
            if solution != '\n':
                step = solution.split("\n")[0]
                if step != '':
                    equations_solution.append(step)
        f.close()

    equations_incorrect = equations_incorrect[0:-1]
    equations_solution = equations_solution

    print(i, equations_incorrect)
    print(i, equations_solution)

    step_0_in_candidates = False
    count = -1
    for eq_incorrect in equations_incorrect:
        count += 1
        for eq_solution in equations_solution:
            if eq_incorrect == eq_solution or rearrange_equation(eq_incorrect) == eq_solution or rearrange_equation(eq_solution) == eq_incorrect:
                step_0_in_candidates = True # print("Step 0 is correct for prompt ", i, ".")
            else:
                step_0_in_candidates = False # print("Solution step 0 is not in candidate step 0's for prompt ", i, ".\nStep 0: ", eq_incorrect, "\nSolution step 0's: ", equations_solution)

    if step_0_in_candidates == False:
        print("Solution step 0 is not in candidate step 0's for prompt ", i)
    
    booleans[i] = step_0_in_candidates

for i in booleans:
    if booleans[i]:
        print(i, "True!") 
