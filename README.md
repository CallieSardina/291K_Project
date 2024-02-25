# 291K_Project

prase_logs.py 

    - parses json log with game information 
    - finds all games which resulted in an incorrect/ impossible result
    - generates prompts we could possibly use to re-prompt GPT on these games (./prompts/prompt_{}.txt)
    - correct solutions for each game GPT lost is also in ./prompts/prompt_{}_solution.txt)
        

- Took out some solutions that involved division with rounding because they didn't all make sense.