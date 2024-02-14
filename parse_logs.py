import json
 
# load contents of json log
f = open('./logs/game24/gpt-4_0.7_propose1_value3_greedy5_start900_end1000.json')
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
        final_ys[game_idx] = (game['ys'], result)
        # get final results for each game
        if result == 1:
            final_result[game_idx] = 1
    if game_idx not in final_result:
        final_result[game_idx] = 0





