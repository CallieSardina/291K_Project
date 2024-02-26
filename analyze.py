import os

import json
import solution_prompts
import parse_logs 


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# load contents of json log
f = open('./gpt-4_0.7_propose1_value3_greedy5_start900_end1000.json')
data = json.load(f)

final_result = {} # map: game index --> win (1) / lose (0)

for game in data:
    # get game index [900-1000]
    game_idx = game['idx']
    if game_idx not in final_result:
        final_result[game_idx] = None

# Get all games which were lost (incorrect / impossible result)
for game_idx in list(final_result.keys()):

    directory = './info/'
    #for i in range(900, 1000):
    step_0 = parse_logs.get_step_0s()[game_idx][0]

    filepath = "./info/step_0s/step_0_" + str(game_idx) + ".txt"
    f = open(filepath, "w")
    f.write(str(step_0))
    f.close()

    numbers = []
    operations = []

    for char in step_0.split(" "):
        if char.isnumeric() or is_float(char):
            numbers.append(char) 
        else:
            operations.append(char)
    numbers = numbers[0:4]
    operations = operations[0:1]

    filepath = "./info/nums_and_ops/nums_and_ops_" + str(game_idx) + ".txt"
    f = open(filepath, "w")
    f.write(str(numbers))
    f.write("\n")
    f.write(str(operations))
    f.close()