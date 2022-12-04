import pandas as pd

filePath = "data/day1"

data = pd.read_table(filePath, header=None, skip_blank_lines=False)

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
