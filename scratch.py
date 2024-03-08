import os

directory_path = "./all_solution_steps/"  

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

for i in range(900, 1000):
    file_name = f"{i}.txt"
    file_path = os.path.join(directory_path, file_name)
    
    with open(file_path, "w") as file:
        file.write("")
