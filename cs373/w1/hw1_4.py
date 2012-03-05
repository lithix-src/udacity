#! /usr/bin/env python

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

def move(w, coords):
    # [0,1] = move right
    # [1,0] = move down
    
# i was right about generating a distribution first, but wrong in how
# use the value of 1.0 / len(world) / len(world[0]) for initial state

    
