import re
from copy import deepcopy

input_file = open('input-5-1.txt')

is_drawing = True
drawing_input = []
drawing2 = drawing1 = []

for line in input_file:
  clean_line = line.replace('\n', '')

  if is_drawing:    
    if len(clean_line) > 0:
      arrangement = [ clean_line[i * 4 + 1] for i in range(0, int((len(clean_line) + 1) /4)) ]
      drawing_input.append(arrangement)      
    else:      
      for i in range(0, len(drawing_input[0])):
        stack = []
        start = len(drawing_input) - 1
        while start >= 0 and drawing_input[start][i] != ' ':
          stack.append(drawing_input[start][i])
          start -= 1
        drawing1.append(stack)
      
      drawing2 = deepcopy(drawing1)
      is_drawing = False

  else:
    rearrangement_regex = re.match('move (\d*) from (\d*) to (\d*)', clean_line)       
    match = rearrangement_regex.groups()

    count = int(match[0])
    source = int(match[1]) - 1
    dest = int(match[2]) - 1

    for i in drawing2[source][-1 * count:]:
      drawing2[dest].append(i)
      drawing1[dest].append(drawing1[source].pop())
      drawing2[source].pop()

print(''.join([drawing1[i][-1] for i in range(0, len(drawing1))]))
print(''.join([drawing2[i][-1] for i in range(0, len(drawing2))]))
