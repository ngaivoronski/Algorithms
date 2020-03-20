#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

list_of_answers = []

def knapsack_helper( items, capacity, answer):
  # go through the list of items of each item and check to see if they fit in your bag
  for item in items:
    # if the item doesn't fit, go on to next item
    if capacity - item.size < 0:
      pass
    # if the item fits, put it in the bag, adjust the value, capacity of the bag and reduce the list of items
    # then rerun the function with the new bag and the new list of items
    else:
      updated_items = [namedtuple for namedtuple in items if namedtuple.index != item.index]
      updated_capactiy = capacity - item.size
      updated_answer = {'Value': answer['Value'] + item.value, 'Chosen': answer['Chosen'] + [item.index]}
      knapsack_helper(updated_items, updated_capactiy, updated_answer)
  
  # if you still have a non-negative capacity and there are no items left, add your answer to the list of answers
  if capacity >= 0:
    list_of_answers.append(answer)

def knapsack_solver(items, capacity):
  # clear the list of answers
  del list_of_answers[ 0:len(list_of_answers) ]

  # set up a blank answer
  answer={'Value': 0, 'Chosen': []}

  # run the function to populate the list of answers
  knapsack_helper(items, capacity, answer)

  # sort the answers by value
  def answer_sort(item):
    return item['Value']
  list_of_answers.sort(key=answer_sort, reverse=True)

  # return the first answer (the highest value)
  return list_of_answers[0]







if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')