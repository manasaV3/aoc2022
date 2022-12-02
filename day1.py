import heapq

calories_by_elf = []

current_calories = 0

with open('input-1-1.txt') as input_file:
  for line in input_file:
    clean_line = line.strip()
    if clean_line == '':
      heapq.heappush(calories_by_elf, current_calories)
      current_calories = 0
    else:
      current_calories += int(clean_line)


## Solution 1:
print(f"Calories for elf with most calories={calories_by_elf[-1]}")

## Solution 2:
print(f"Calories for top 3 elves with most calories={sum(calories_by_elf[-3:])}")