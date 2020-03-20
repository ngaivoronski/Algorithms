#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients, count=0):
  # run through the list of keys in the recipe
  for i in recipe.keys():
    try:
      # check to see if there are enough ingredients to cover each element of recipe
      if ingredients[i] >= recipe[i]:
        ingredients[i] -= recipe[i]
      else:
        return count
    # check if you're missing an ingredient
    except KeyError:
      return count

  # if there are enough ingredients - iterate the batch number and run function again
  count += 1
  return recipe_batches(recipe, ingredients, count)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))