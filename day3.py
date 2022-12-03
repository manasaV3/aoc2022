import string 

def generate_map(offset, source):
  return {x:ord(x) - offset  for x in  list(source)}

PRIORITY_MAP = { **generate_map(ord('a') - 1, string.ascii_lowercase), 
                **generate_map(ord('A') - 27, string.ascii_uppercase)}            

input_file = open('input-3-1.txt')

total_score1 = 0
total_score2 = 0

common = {}
line_count = 0

for line in input_file:
  clean_line = line.strip()
  partition_size = int(len(clean_line)/2)
  second_half = set(clean_line[partition_size:])
  mismatched = next(filter(lambda x: x in second_half, clean_line[:partition_size]))

  total_score1 += PRIORITY_MAP[mismatched]

  line_count += 1

  if line_count % 3 == 1:
    common = set(clean_line)
  else:
    common = common.intersection(set(clean_line))
  
  if line_count % 3 == 0:
    total_score2 += PRIORITY_MAP[common.pop()]
        

print(f"total_score1={total_score1}")
print(f"total_score2={total_score2}")