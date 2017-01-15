__author__ = 'philippe'
import World
import threading
import time
import random

discount = 0.3
actions = World.actions
states = []

#stuff I really need to care about
#World.x and World.Y are the dimentions fo the grid
#Q and states are what I would imagine them to be
#World.specials is important
#World.set_cell_Score is an imp function


Q = {}
#let me first create the Q grid
#then populate that with the scores


def do_action(action):
    #print "in do action"
    #right now, we are set up to move randomly. 
    action = random.choice(World.actions)
    print "Action is : " + action
    if action == actions[0]:
        World.try_move(0, -1)
    elif action == actions[1]:
        World.try_move(0, 1)
    elif action == actions[2]:
        World.try_move(-1, 0)
    elif action == actions[3]:
        World.try_move(1, 0)
    else:
        return
    return action

#return max action, max val
def max_Q(s):
    a = 1
    #print "in max q"

def inc_Q(s, a, alpha, inc):
    b = 1
    #print "in inc"
def run():
    time.sleep(1)
    alpha = 1
    t = 1
    while True:
        # Pick the right action
        s = World.player
        max_Q(s)
        do_action(s)
        #inc_Q(s, a, alpha, r + discount * max_val)

        time.sleep(0.5)

t = threading.Thread(target=run)
t.daemon = True
t.start()
World.start_game()
