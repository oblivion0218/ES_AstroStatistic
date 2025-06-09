import numpy as np
import random
import matplotlib.pyplot as plt


n=100000 # Number of simulations
N=5 #Number of doors
conservative=[]
swticher=[]
newcomer=[]
M_value=[]

for M in range (1,N-1):
    cons=0
    new=0
    swt=0
    for i in range (n):
        doors=np.zeros(N) #N doors, 1 with the car the other with goat
        pos=random.randint(0,N-1) # Position of the prize
        doors[pos]=1
        choice=np.zeros(N) #Vector of choices
        c=random.randint(0,N-1) # The door initially chosen by the player 
        choice[c]=1


        for j in range (M):
            a=random.randint(0,N-1)
            while choice[a]!=0 or doors[a]!=0:  #He can't open the door chosen, the door with the prize and a door already opened
                a=random.randint(0,N-1)
            doors[a]=-1
            choice[a]=-1
        

        cons+= doors[c] #The cons keeps his choice 


        b=random.randint(0,N-1)
        while doors[b]==-1:
            b=random.randint(0,N-1)
        new+= doors[b]   #The new chooses one of the remaining doors, not the open one
        

        for h in range (N):
            if choice[h]==0:
                swt+= doors[h]  #The swticher changes the door, not the open one nor the one chosen at the beginning 
                break   #Break because at the first doors not chosen 

    conservative.append(cons/n)
    swticher.append(swt/n)
    newcomer.append(new/n)
    M_value.append(M)

for i in range(0,N-2):
    print("Number of doors", M_value[i])
    print("Probability of winning for the conservative",conservative[i])
    print("Probability of winning for the newcomer",newcomer[i])
    print("Probability of winning for the swticher",swticher[i])


plt.plot(M_value, conservative, "-o", label="conservative")
plt.plot(M_value, swticher, "-o", label="swticher")
plt.plot(M_value, newcomer, "-o", label="newcomer")
plt.title("%i doors" %N)
plt.legend()
plt.savefig("MontyhallGEN.png")



