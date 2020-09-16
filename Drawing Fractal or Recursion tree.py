#Jaya Chand
#16/09/2020

"""
Drawing Fractal or Recursion tree
Using turtle to plot fractal and recursion trees
"""

import turtle ##using turtle to plot output
hr=turtle.Turtle()
hr.left(90)
hr.speed(150)

def tree(i):
  if i<10:
    exit
  else:
    hr.forward(i)
    hr.left(30)
    tree(3*i/4)
    hr.right(60)
    tree(3*i/4)
    hr.left(30)
    hr.backward(i)


tree(50)