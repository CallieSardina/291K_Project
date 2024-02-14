import json
 
# load contents of json log
f = open('./logs/game24/gpt-4_0.7_propose1_value3_greedy5_start900_end1000.json')
data = json.load(f)

x_input_numbers = {} # map: game index --> 4 input numbers
step_0 = {} # map: game index --> (new_y, value, selected (0 = no, 1 = yes)) list - for step 0
step_1 = {} # map: game index --> (new_y, value, selected (0 = no, 1 = yes)) list - for step 1
step_2 = {} # map: game index --> (new_y, value, selected (0 = no, 1 = yes)) list - for step 2
step_3 = {} # map: game index --> (new_y, value, selected (0 = no, 1 = yes)) list - for step 3

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
        if step == 0:
            step_0[game_idx] = (candidate_ys, values, new_ys)
        elif step == 1:
            step_1[game_idx] = (candidate_ys, values, new_ys)
        elif step == 2:
            step_2[game_idx] = (candidate_ys, values, new_ys)
        else:
            step_3[game_idx] = (candidate_ys, values, new_ys)

