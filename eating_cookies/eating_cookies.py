#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None, count=0):
  # set up a cache if there isn't one
  if not cache:
    return eating_cookies(n, [0 for i in range(0,n+1)], 0)
  # check cache to see if you've already solved the recursive problem
  elif cache[n] > 0:
    return cache[n]
  # if there's nothing in the cache and you still have cookies try eating 1, 2, or 3 at a time
  elif n > 0:
    cache[n] = (eating_cookies(n-3, cache, count) + eating_cookies(n-2, cache, count) + eating_cookies(n-1, cache, count))
    return cache[n]
  # if there are no cookies left, add 1 to your count
  elif n == 0:
    count = count + 1
    return count
  # if you hit a negative, it means you went over, return count as is
  else:
    return count

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')