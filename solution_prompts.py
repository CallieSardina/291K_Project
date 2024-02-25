import os

def gen_solution_prompt(index):
    directory = './solution_steps/'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename[7: 10] == str(index):
            with open(f, 'r') as fn:
                prompt = """For reference in the analysis of where the error occurred, 
                        I have provided the correct sequence of operations to reach 24 is listed below. 
                        If there are multiple possible solution paths, these are delimited by '***'.
                        Please use this information to determine where you made your previous mistake.""" + "\n" + fn.read()
    return prompt



