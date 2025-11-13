import math

def euclid(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2- y1
  return math.sqrt(dx * dx + dy * dy)

def manhattan(x1, y1, x2, y2):
  return abs(x2 - x1) + abs(y2 - y1)
