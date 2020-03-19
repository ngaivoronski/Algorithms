#!/usr/bin/python

import sys

def making_change(amount, denominations, cache=None):
  # set up a cache if there isn't one
  if not cache:
    cache = [0 for i in range(0, amount+1)]
    cache[0] = 1
    return making_change(amount, denominations, cache)
    
  # check cache to see if you've already solved the recursive problem
  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      difference = higher_amount - coin
      cache[higher_amount] += cache[difference]
  
  return cache[amount]

# def making_change(amount, denominations):
#   if amount == 0:
#     return 1
#   if amount < 0:
#     return 0
#   if len(denominations) <= 0 and amount > 0:
#     return 0
#   else:
#     return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")