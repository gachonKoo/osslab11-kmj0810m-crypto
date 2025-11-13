import math

def euclidean(x1, y1, x2, y2):
  return math.dist([x1, y1], [x2, y2])

def manhattan(x1, y1, x2, y2):
  return abs(x2 - x1) + abs(y2 - y1)
