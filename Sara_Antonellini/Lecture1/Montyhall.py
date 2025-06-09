import numpy as np
import random
import matplotlib.pyplot as plt

N = 50000 # Number of simulations
conservative=0
switcher=0
newcomer=0
for i in range(N):
    doors=np.array([0,0,0]) #three doors,1 car,2 goats
    choice=np.array([0,0,0]) #vector of choices
    pos=random.randint(0,2) # Position of the prize
    doors[pos]=1
    c=random.randint(0,2) # The door initially chosen by the player 
    choice[c]=1

    a=random.randint(0,2) #Randomic generation of the position of the door to be opened
    while a==pos or a==c : #The position can't be the position of the prize or the chosen position
        a=random.randint(0,2)
    door_opened=a
    doors[a]=-1
    choice[a]=-1 

    conservative+=doors[c] #The conservative keeps his choice 

    b=random.randint(0,2)
    while doors[b]==-1:
        b=random.randint(0,2)
    newcomer+=doors[b] #The newcomer chooses one of the two remaining doors, not the open one


    for j in range(3):
        if choice[j]==0:
            switcher+=doors[j] #The swticher changes the door, not the open one nor the one chosen at the beginning



print("Probability of winning for the conservative", conservative/N)
print("Probability of winning for the swticher", switcher/N)
print("Probability of winning for the newcomer", newcomer/N)

