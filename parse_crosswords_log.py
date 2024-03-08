import json
import solution_prompts

f = open('./no_prune_games_that_prune_won.json')
data_no_prune = json.load(f)
f.close()

# print(data_no_prune)

f = open('./prune_correct.json')
data_prune = json.load(f)
f.close()


for game_idx in [1, 6, 7, 8, 12, 13, 18]:
    first_dif = None
    print("___________________________________________")
    highest_word_score = 0
    highest_word_score_idx = None
    steps = data_no_prune[str(game_idx)]
    for step_idx, step in enumerate(steps):
        #print(step)
        if step['actions'] == data_prune[str(game_idx)][step_idx]['actions']:
            print("here")
            print(step)
            print(data_prune[str(game_idx)][step_idx])
            print()
            print(steps[step_idx + 1])
            print(data_prune[str(game_idx)][step_idx + 1])
            dif = [x for x in steps[step_idx + 1]['actions'] if x not in set(data_prune[str(game_idx)][step_idx + 1]['actions'])]
            print("dif", dif, len(dif))
            if dif != []:
                first_dif = dif[-1]
                print("first dif", first_dif)
            print()
        if data_prune[str(game_idx)][step_idx]["info"]["r_word"] == 1.0:
            print("answer")
            print(data_prune[str(game_idx)][step_idx])
            print()
        if steps[step_idx]["info"]["r_word"] > highest_word_score:
            highest_word_score = steps[step_idx]["info"]["r_word"] 
            highest_word_score_idx = step_idx
        for clue in step["actions"]:
            if first_dif != None:
                if clue.split('.')[0] == first_dif.split('.')[0]:
                    if clue.split('.')[1] == first_dif.split('.')[1]:
                        print("No parse gets this part right later at step", step_idx)
    print("high score no prune", highest_word_score, steps[highest_word_score_idx])
# # load contents of json log
# f = open('./infoss_dfs_no_prune.json')
# data_no_prune = json.load(f)

# f = open('./infoss_dfs_prune.json')
# data_prune = json.load(f)

# game_count = 0

# games_won = {}

# for game in data:
#     for step in game:

#         # if step['info']['r_word'] == 1.0:
#         if game_count in [1, 6, 7, 8, 12, 13, 18]:
#             games_won[game_count] = game

#     game_count += 1 


# print(list(games_won.keys()))
# with open('no_prune_games_that_prune_won.txt', 'w') as f: 
#      f.write(json.dumps(games_won))