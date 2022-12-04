
def to_range(input):
  return tuple(map(int, input.split('-')))


def is_complete_overlap(section1, section2):
  return (section1[0] <= section2[0] and section1[1] >= section2[1]) or \
    (section2[0] <= section1[0] and section2[1] >= section1[1])

def is_overlap(section1, section2):
  return (section1[0] <= section2[0] and section1[1] >= section2[0]) or \
    (section1[0] <= section2[1] and section1[1] >= section2[1]) or \
    (section2[0] <= section1[0] and section2[1] >= section1[0]) or \
    (section2[0] <= section1[1] and section2[1] >= section1[1])

complete_overlap_count = 0
overlap_count = 0

input_file = open('input-4-1.txt')

for line in input_file:
  clean_line = line.strip()
  section_ranges = list(map(to_range, clean_line.split(',')))

  if is_complete_overlap(section_ranges[0], section_ranges[1]):
    complete_overlap_count += 1

  if is_overlap(section_ranges[0], section_ranges[1]):
    overlap_count += 1


print(f"Total number of sections with complete_overlap={complete_overlap_count}")
print(f"Total number of sections with overlap={overlap_count}")