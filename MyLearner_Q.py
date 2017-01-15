__author__ = 'philippe_modified_aditya'
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
for i in range(0, World.x):
    for j in range(0, World.y):
        temp = {}
        for action in World.actions:
            temp[action] = 0.1
        Q[(i, j)] = temp


#for item in World.specials:
#    Q[item[0], item[1]] = item[3]

#print Q
#print len(Q)
#exit()
#let me first create the Q grid
#then populate that with the scores


def do_action(action):
    #print "in do action"
    #right now, we are set up to move randomly. 
    #action = random.choice(World.actions)
    s = World.player
    r = -World.score
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
    
    s2 = World.player
    r += World.score
    return s, action, r, s2


#return max action, max val
def max_Q(s):
    action = None
    vals = []
    
    for a, q in Q[s].items():
        if len(vals) == 0:
            vals.append([a, q])
        elif q > vals[0][1]:
            vals = []
            vals.append([a, q])
        elif q == vals[0][1]: 
            vals.append([a, q])
            
            #print vals
            #exit()

    print vals

    val = random.choice(vals)
    print vals
    print "-------"
    #exit()
    return val[0], val[1]
    #print "in max q"

def inc_Q(s, a, alpha, inc):
    Q[s][a] = alpha * Q[s][a] + (1 - alpha) * inc
    World.set_cell_score(s, a, Q[s][a])
    print s
    print a
    print Q[s][a]
    print ""
    b = 1
    #print "in inc"
def run():
    time.sleep(1)
    alpha = 1
    t = 1
    while True:
        # Pick the right action
        s = World.player
        a, q = max_Q(s)
        s, a, r, s2 = do_action(a)
        if s2 not in (World.specials):
            a2, q2 = max_Q(s2)
        else:
            a2, q2 = a, q
        print s
        print a
        print r
        print "---"
        inc_Q(s, a, 0.5, r + discount * q2)
        print "--------------pretty print-------------"
        for j in range(0, World.y):
            
            for action in World.actions:
                strtemp = ""
                for i in range(0, World.x):
                    strtemp = strtemp +  "        " + action + ":" + str(round(Q[(i, j)][action], 3))
                print strtemp
            print "-------"
        time.sleep(.1)

t = threading.Thread(target=run)
t.daemon = True
t.start()
World.start_game()
