import re
import os



def split_equation(equation):
    numbers = list(map(int, re.findall(r'\b\d+\b', equation)))
    operations = re.findall(r'[+\-*/]', equation)

    if len(numbers) != 4 or len(operations) != 3:
        raise ValueError("Invalid equation format. Please provide an equation with 4 numbers and 3 operations.")

    result_1 = int(numbers[0])
    result_2 = int(eval(f"{numbers[0]} {operations[0]} {numbers[1]}"))
    result_3 = int(eval(f"{result_2} {operations[1]} {numbers[2]}"))
    result_final = int(eval(f"{result_3} {operations[2]} {numbers[3]}"))

    step1 = f"{numbers[0]} {operations[0]} {numbers[1]} = {result_2}"
    step2 = f"{result_2} {operations[1]} {numbers[2]} = {result_3}"
    step3 = f"{result_3} {operations[2]} {numbers[3]} = {result_final}"

    # print(f"{numbers[0]} {operations[0]} {numbers[1]} = {result_2}")
    # print(f"{result_2} {operations[1]} {numbers[2]} = {result_3}")
    # print(f"{result_3} {operations[2]} {numbers[3]} = {result_final}")

    return step1, step2, step3


directory = './prompts/'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and len(filename.split('_')) > 2:
        if filename.split('_')[2] == 'solution.txt':
            with open(f, 'r') as fn:
                equations = fn.readlines() 
                for equation in equations:
                    if equation != '' and equation != '\n':
                        eq = equation.split(']')[1]
                        step1, step2, step3 = split_equation(eq)
                        filepath = filename[:-4] + "_steps.txt"
                        f = open(filepath, "a") 
                        f.write(step1)
                        f.write("\n")
                        f.write(step2)
                        f.write("\n")
                        f.write(step3)
                        f.write("\n")
                        f.write("***")
                        f.write("\n")
                        f.close()




