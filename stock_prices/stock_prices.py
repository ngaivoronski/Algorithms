#!/usr/bin/python

import argparse

# set up index at 0 and profit at negative inf
def find_max_profit(prices, index=0, profit=float("-inf")):
  
  # compare each (sell) value of array to the value of the index (buy)
  # if the buy number is after sell and the profit would be greater than current profit, update the profit
  for i in range(0, len(prices)):
    if prices[i] - prices[index] > profit and i > index:
      profit = prices[i] - prices[index]
  
  # iterate index (buy number)
  index += 1

  # if the index is still within the array, run the function again
  if index < len(prices):
    return find_max_profit(prices, index, profit)
  else:
    return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))