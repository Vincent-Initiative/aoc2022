import pandas as pd

data = pd.read_table("input.txt", header=None, skip_blank_lines=False)

max_calories = 0
current_calories = 0
for calories in data[0]:
    if(pd.isna(calories)):
        if(current_calories > max_calories):
            max_calories = current_calories
        current_calories = 0
    else:    
        current_calories += calories
        
print(max_calories)
