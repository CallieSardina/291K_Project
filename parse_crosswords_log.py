import json
import solution_prompts

# load contents of json log
f = open('./infoss_dfs_no_prune.json')
data = json.load(f)

game_count = 0

games_won = {}

for game in data:
    for step in game:

        if step['info']['r_word'] == 1.0:
            games_won[game_count] = game

    game_count += 1 


print(list(games_won.keys()))