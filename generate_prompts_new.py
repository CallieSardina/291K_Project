import json
import solution_prompts

# load contents of json log
f = open('./gpt-4_0.7_propose1_value3_greedy5_start900_end1000.json')
data = json.load(f)

x_input_numbers = {} # map: game index --> 4 input numbers
step_0 = {} # map: game index --> (candidate_y, value, selected (0 = no, 1 = yes)) list - for step 0
step_1 = {} # map: game index --> (candidate_y, value, selected (0 = no, 1 = yes)) list - for step 1
step_2 = {} # map: game index --> (candidate_y, value, selected (0 = no, 1 = yes)) list - for step 2
step_3 = {} # map: game index --> (candidate_y, value, selected (0 = no, 1 = yes)) list - for step 3
final_ys = {} # map: game index --> final ys with all 4 equations and if they equal 24 (ys, ==24?1:0)
final_result = {} # map: game index --> win (1) / lose (0)

for game in data:
    # get game index [900-1000]
    game_idx = game['idx']

    # x = 4 input numbers
    x = game['steps'][0]['x']
    x_input_numbers[game_idx] = x

    # fill game index --> step results dictionaries with results/ steps
    for step in range(4):
        candidate_ys = game['steps'][step]['new_ys']
        values = game['steps'][step]['values']
        new_ys = game['steps'][step]['select_new_ys']
        for i in range(len(candidate_ys)):
            if candidate_ys[i] in new_ys:
                selected = 1
            else:
                selected = 0
            if step == 0:
                step_0[game_idx] = (candidate_ys[i][:-1], values[i], selected) # added the [:-1] to take off the newline character
            elif step == 1:
                step_1[game_idx] = (candidate_ys[i][:-1], values[i], selected)
            elif step == 2:
                step_2[game_idx] = (candidate_ys[i][:-1], values[i], selected)
            else:
                step_3[game_idx] = (candidate_ys[i][:-1], values[i], selected)

    # get final ys and results (correct/ incorrect)
    ys = game['ys']
    for i in range(len(ys)):
        result = game['infos'][i]['r']
        if game_idx not in final_ys:
            final_ys[game_idx] = [(game['ys'][i], result)]
        else:
            final_ys[game_idx].append((game['ys'][i], result))
        # get final results for each game
        if result == 1:
            final_result[game_idx] = 1
    if game_idx not in final_result:
        final_result[game_idx] = 0

# Get all games which were lost (incorrect / impossible result)
for game_idx in list(final_result.keys()):
    if final_result[game_idx] == 0:
        tmp_x = x_input_numbers[game_idx]
        tmp_ys = final_ys[game_idx]
        for i in range(len(tmp_ys)):
            equations = tmp_ys[i][0].split("\n")
            f = open("games_lost.txt", "w")
            f.write(tmp_x)
            f.write("\n")
            f.write(str(tmp_ys[i]))
            f.write("\n")
            f.close()
        tmp = []
        for eq in equations:
            if eq != '':
                tmp.append(eq)
        equations = tmp
        if len(equations) == 4:
            equation1 = equations[0]
            equation2 = equations[1]
            equation3 = equations[2]
            equation4 = equations[3]
            prompt = """You were previously given the following instructions: 
                Use numbers and basic integer arithmetic operations (+ - * /) to obtain 24. You may only use three equations to reach the answer, and you should never get an intermediate decimal value. 
                At each subsequent step, you were prompted to evaluate if given numbers can reach 24 (sure/likely/impossible).
                At the final step, you were given an input and an answer and instructed to give a judgement (sure/impossible) if the answer is correct, 
                i.e. it uses each input exactly once and no other numbers, and reach 24.

                For an input of the form (x x x x), follow the below structure to format your answer:
                
                Input: x x x x 

                Equation 1: x (operation) x = a
                Equation 2: x (operation) a = b or a (operation) x = b 
                Equation 3: x (operation) b = 24 or b (operation) x = 24

                You can use the inputs in any order, but each input may only be used once. 
                You may use basic arithmetic operations +,-,*,/.
            
                Given the numbers """ + str(tmp_x) + """, your initial output was that it is impossible to reach 24. 
                Let\'s explore the thought process and identify where the error occurred. Break down your solution into individual steps, 
                explaining the reasoning behind each operation.

                Start by reviewing the initial input """ + str(tmp_x) + """.
                The first operation you used was """ + str(equation1) + """ 
                Explain the first operation performed and its purpose. 
                That is, explain why you chose these numbers and corresponding operation to start with as opposed to any other combination.
                If an error occurred in the first step, identify the correct operation that should have been chosen.
                Continue this process step by step until the incorrect output is reached.
                The second operation you used was """ + str(equation2) + """.
                The third operation you used was """ + str(equation3) + """.
                You provided a fourth step (which is nto permitted). It was """ + str(equation4) + """.
                Start from the final step, and determine if you could change this step to reach a correct solutions resulting in 24.
                Given this information, reevaluate, then repeat this analysis for the second step and first step as necessry.
                For each step, provide the correct operation and the correct subsequent operations and result.
                Conclude by summarizing the correct sequence of operations that lead to the correct solution for the game of 24, and report the solution
                in the following format, remember that you can only use 3 equations to reach 24:

                [Equation 1]: 
                [Equation 2]:
                [Equation 3]: 

                Evaluate whether your new response correctly evaluates to 24.""" 
                # If it does not, review the following: """ + "\n" + solution_prompts.gen_solution_prompt(game_idx)

        elif len(equations) == 3:
            equation1 = equations[0]
            equation2 = equations[1]
            equation3 = equations[2]
            prompt = """You were previously given the following instructions: 
                Use numbers and basic integer arithmetic operations (+ - * /) to obtain 24. You may only use three equations to reach the answer, and you should never get an intermediate decimal value. 
                At each subsequent step, you were prompted to evaluate if given numbers can reach 24 (sure/likely/impossible).
                At the final step, you were given an input and an answer and instructed to give a judgement (sure/impossible) if the answer is correct, 
                i.e. it uses each input exactly once and no other numbers, and reach 24.
            
                For an input of the form (x x x x), follow the below structure to format your answer:
                
                Input: x x x x 

                Equation 1: x (operation) x = a
                Equation 2: x (operation) a = b or a (operation) x = b 
                Equation 3: x (operation) b = 24 or b (operation) x = 24

                You can use the inputs in any order, but each input may only be used once. 
                You may use basic arithmetic operations +,-,*,/.

                Given the numbers """ + str(tmp_x) + """, your initial output was that it is impossible to reach 24. 
                Let\'s explore the thought process and identify where the error occurred. Break down your solution into individual steps, 
                explaining the reasoning behind each operation.

                Start by reviewing the initial input """ + str(tmp_x) + """.
                The first operation you used was """ + str(equation1) + """ 
                Explain the first operation performed and its purpose. 
                That is, explain why you chose these numbers and corresponding operation to start with as opposed to any other combination.
                If an error occurred in the first step, identify the correct operation that should have been chosen.
                Continue this process step by step until the incorrect output is reached.
                The second operation you used was """ + str(equation2) + """.
                The third operation you used was """ + str(equation3) + """.
                After the third operation, you deemed it impossible to reach 24 with the given input numbers.
                Start from the third step, and determine if you could change this step to reach a correct solutions resulting in 24.
                Given this information, reevaluate, then repeat this analysis for the second step and first step as necessry.
                For each step, provide the correct operation and the correct subsequent operations and result.
                Conclude by summarizing the correct sequence of operations that lead to the correct solution for the game of 24, and report the solution
                in the following format, remember that you can only use 3 equations to reach 24:
                
                [Equation 1]: 
                [Equation 2]:
                [Equation 3]: 

                Evaluate whether your new response correctly evaluates to 24.""" 
                # If it does not, review the following: """ + "\n" + solution_prompts.gen_solution_prompt(game_idx)

        filepath = "./new_prompt_testing/prompt_" + str(game_idx) + ".txt"
        f = open(filepath, "w")
        f.write(prompt)
        f.close()




