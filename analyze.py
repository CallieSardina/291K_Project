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

final_results = parse_logs.get_final_results()
wins = []
losses = []
for game_idx in list(final_results.keys()):
    if final_results[game_idx] == 1:
        wins.append(game_idx)
    else:
        losses.append(game_idx)

add_count = 0
sub_count = 0
mult_count = 0
div_count = 0

add_count_win = 0
sub_count_win = 0
mult_count_win = 0
div_count_win = 0

add_count_loss = 0
sub_count_loss = 0
mult_count_loss = 0
div_count_loss = 0

for game_idx in list(final_result.keys()):

    directory = './info/'
    #for i in range(900, 1000):

    step_0s = parse_logs.get_step_0s()
    for i in step_0s:
        #step_0 = parse_logs.get_step_0s()[game_idx][0]
        with open("./info/step_0s/step_0_" + str(game_idx) + ".txt", "w") as f:
            for triple in step_0s[i]:
                f.write(str(triple))
                f.write("\n")

#     numbers = []
#     operations = []

#     for char in step_0.split(" "):
#         if char.isnumeric() or is_float(char):
#             numbers.append(char) 
#         else:
#             operations.append(char)
#     numbers = numbers[0:3]
#     operation = operations[0]

#     if operation == '+': 
#         add_count += 1
#     if operation == '-': 
#         sub_count += 1
#     if operation == '*': 
#         mult_count += 1
#     if operation == '/': 
#         div_count += 1

#     if game_idx in wins:
#         if operation == '+': 
#             add_count_win += 1
#         if operation == '-': 
#             sub_count_win += 1
#         if operation == '*': 
#             mult_count_win += 1
#         if operation == '/': 
#             div_count_win += 1

#     if game_idx in losses:
#         if operation == '+': 
#             add_count_loss += 1
#         if operation == '-': 
#             sub_count_loss += 1
#         if operation == '*': 
#             mult_count_loss += 1
#         if operation == '/': 
#             div_count_loss += 1


#     filepath = "./info/nums_and_ops/nums_and_ops_" + str(game_idx) + ".txt"
#     f = open(filepath, "w")
#     f.write(str(numbers))
#     f.write("\n")
#     f.write(str(operation))
#     f.close()

# filepath = "./info/total_operation_counts.txt"
# f = open(filepath, "w")
# f.write(str(add_count))
# f.write("\n")
# f.write(str(sub_count))
# f.write("\n")
# f.write(str(mult_count))
# f.write("\n")
# f.write(str(div_count))
# f.write("\n")
# f.close()

# filepath = "./info/win_operation_counts.txt"
# f = open(filepath, "w")
# f.write(str(add_count_win))
# f.write("\n")
# f.write(str(sub_count_win))
# f.write("\n")
# f.write(str(mult_count_win))
# f.write("\n")
# f.write(str(div_count_win))
# f.write("\n")
# f.close()


# filepath = "./info/loss_operation_counts.txt"
# f = open(filepath, "w")
# f.write(str(add_count_loss))
# f.write("\n")
# f.write(str(sub_count_loss))
# f.write("\n")
# f.write(str(mult_count_loss))
# f.write("\n")
# f.write(str(div_count_loss))
# f.write("\n")
# f.close()

