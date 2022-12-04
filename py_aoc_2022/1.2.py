import pandas as pd
import heapq

filePath = "data/day1"

data = pd.read_table(filePath, header=None, skip_blank_lines=False)

top3_calories = [0, 0, 0]
current_calories = 0

for calories in data[0]:
    if(pd.isna(calories)):
        if (current_calories>heapq.nsmallest(1, top3_calories)[0]):
            heapq.heapreplace(top3_calories, current_calories)
        current_calories = 0
    else:    
        current_calories += calories
        
print(sum(top3_calories))
