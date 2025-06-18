import numpy as np
import random
import matplotlib.pyplot as plt

doors = np.array([0,0,0]) #three doors
N = 50000  # Number of simulations

win_switch = 0  # Wins when switching doors
win_no_switch = 0  # Wins without switching doors
loss_switch = 0  # Losses when switching doors
loss_no_switch = 0  # Losses without switching doors

for i in range(N):

    position=random.randint(0,2)  # Position of the prize
    doors[position] = 1 # put the car behind the door
    scelta = random.randint(0,2) # The door initially chosen by the player
    change = random.randint(0,1) # 0 = doesn't switch, 1 = switches


    #Player doesn't switch
    if scelta == position and change == 0 :
        win_no_switch += 1
    elif scelta != position and change == 0:
        loss_no_switch +=1
    
    #Player switch
    if scelta == position and change == 1 :
        loss_switch += 1
    elif scelta != position and change == 1 :
        win_switch += 1   


prob_no_switch = win_no_switch / (win_no_switch + loss_no_switch)
prob_switch = win_switch / (win_switch + loss_switch)
print(f"Probability of winning without switch: {prob_no_switch:.4f}")
print(f"Probability of winning with switch: {prob_switch:.4f}")












    

