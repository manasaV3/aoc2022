import collections

WIN_SCORE, DRAW_SCORE, LOOSE_SCORE = 6, 3, 0

Move = collections.namedtuple('Move',['points','beats'])

ROCK = Move(points=1, beats=[])
PAPER = Move(points=2, beats=[ROCK])
SCISSOR = Move(points=3, beats=[PAPER])
ROCK.beats.append(SCISSOR)


GUIDE_TO_MOVE = {
  'A': ROCK,
  'B': PAPER,
  'C': SCISSOR,
  'X': ROCK,
  'Y': PAPER,
  'Z': SCISSOR,
}
ALL_MOVES = [ROCK, PAPER, SCISSOR]
GUIDE_TO_RESULT = {
  'X': (LOOSE_SCORE, lambda move: move.beats[0]),
  'Y': (DRAW_SCORE, lambda move: move),
  'Z': (WIN_SCORE, lambda move: next(filter(lambda x: move != x and x not in move.beats, ALL_MOVES)))
}


input_file = open('input-2-1.txt')

total_score_sol1 = 0
total_score_sol2 = 0

for line in input_file:
  plays = line.strip().split(' ')
  opponent_move = GUIDE_TO_MOVE[plays[0]]
  column2 =plays[1]


  my_move = GUIDE_TO_MOVE[column2]
  if opponent_move in my_move.beats:
    total_score_sol1 += WIN_SCORE
  elif my_move == opponent_move:
    total_score_sol1 += DRAW_SCORE
  total_score_sol1 += my_move.points


  guide_to_result = GUIDE_TO_RESULT[column2]
  my_potential_move = guide_to_result[1](opponent_move)
  total_score_sol2 += guide_to_result[0] + my_potential_move.points


# Solution 1
print(f"score on following strategy guide as moves {total_score_sol1}")
# Solution 2
print(f"score on following strategy guide as results {total_score_sol2}")
