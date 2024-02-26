import os

def gen_solution_prompt(index):
    directory = './solution_steps/'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename[7: 10] == str(index):
            with open(f, 'r') as fn:
                equation_3 = fn.read().split("***")[0].split("\n")[2]
                prompt = equation_3 + """. Use this information to reason about how to reach this final conclusion, and determine the 
                first two steps in solving this game of 24."""
                # prompt = """For reference in the analysis of where the error occurred, 
                        # I have provided the correct sequence of operations to reach 24 is listed below. 
                        # If there are multiple possible solution paths, these are delimited by '***'.
                        # Please use this information to determine where you made your previous mistake, 
                        # and report why you made the error you did. Explore properties of the numbers and equations,
                        # why your decision making process was faulty, and how it could be improved. 
                        # Report your new answer in the form: 
                        # [Equation 1]
                        # [Equation 2]
                        # [Equation 3].""" + "\n" + fn.read()
    return prompt





