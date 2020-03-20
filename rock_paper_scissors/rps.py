#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  else:
    temparr = []
    for i in rock_paper_scissors(n-1):
      temparr.append(i + ['rock'])
      temparr.append(i + ['paper'])
      temparr.append(i + ['scissors'])
    return temparr


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')