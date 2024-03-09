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
f = open('./gpt-3.5-turbo_0.7_propose1_value3_greedy5_start900_end1000.json')
data = json.load(f)

final_result = {} # map: game index --> win (1) / lose (0)

for game in data:
    # get game index [900-1000]
    game_idx = game['idx']
    if game_idx not in final_result:
        final_result[game_idx] = None

# Get all games which were lost (incorrect / impossible result)

final_results = parse_logs.get_final_results()
wins = []
losses = []
for game_idx in list(final_results.keys()):
    if final_results[game_idx] == 1:
        wins.append(game_idx)
    else:
        losses.append(game_idx)


for game_idx in list(final_result.keys()):

    directory = './our_test_runs/initial_steps/'
    #for i in range(900, 1000):

    step_0s = parse_logs.get_step_0s()
    for i in step_0s:
        #step_0 = parse_logs.get_step_0s()[game_idx][0]
        if str(i) == str(game_idx):
            with open("./our_test_runs/initial_steps/step_0_" + str(game_idx) + ".txt", "w") as f:
                for triple in step_0s[i]:
                    f.write(str(triple[0].split("(")[0][:-1]))
                    f.write("\n")

