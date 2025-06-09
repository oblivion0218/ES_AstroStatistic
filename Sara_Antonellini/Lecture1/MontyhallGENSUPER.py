import numpy as np
import random
import matplotlib.pyplot as plt


n=100000 # Number of simulations
N=6 #Number of doors

# Loop over different door counts (N)
for num in range (3,N): 
    conservative=[]
    swticher=[]
    newcomer=[]
    M_value=[]

    # Loop over different M (number of doors opened by the host)
    for M in range (1,num-1): 
        cons=0
        new=0
        swt=0

        # Simulate n times
        for i in range (n):
            doors=np.zeros(num) # 0 = goat, 1 = car
            pos=random.randint(0,num-1) # Position of the prize
            doors[pos]=1
            choice=np.zeros(num) # Player's initial choice
            c=random.randint(0,num-1) # The door initially chosen by the player 
            choice[c]=1

            # Host opens M doors
            for j in range (M):
                a=random.randint(0,num-1)
                while choice[a]!=0 or doors[a]!=0:  #The host can't open the player's door or the door with the prize
                    a=random.randint(0,num-1)
                doors[a]=-1
                choice[a]=-1
            

            cons+= doors[c] #The conservative keeps his choice 


            b=random.randint(0,num-1)
            #The newcomer chooses one of the remaining doors, not the open ones
            while doors[b]==-1:   
                b=random.randint(0,num-1)
            new+= doors[b]   
            
             
            remaining_doors=[]
            for h in range (num):
                if choice[h]==0:  # The switcher chooses a random door from those that haven't been opened or chosen
                    remaining_doors.append(h) 
            swt += doors[random.choice(remaining_doors)] # Choose a random door from remaining options

        # Store the probabilities of winning for each strategy
        conservative.append(cons/n)
        swticher.append(swt/n)
        newcomer.append(new/n)
        M_value.append(M)


    print("Number of doors", num)
    for i in range(0,num-2):
        print("Number of doors opened", M_value[i])
        print("Probability of winning for the conservative",conservative[i])
        print("Probability of winning for the newcomer",newcomer[i])
        print("Probability of winning for the swticher",swticher[i])
    
    plt.plot(M_value, conservative, "-o", label="conservative")
    plt.plot(M_value, swticher, "-o", label="swticher")
    plt.plot(M_value, newcomer, "-o", label="newcomer")
    plt.xticks(np.arange(min(M_value), max(M_value) + 1, 1))
    plt.title("%i doors" %num)
    plt.legend()
    plt.savefig(f"MontyhallGEN_{num}.png")
    plt.close() 


"""for h in range (num):
                if choice[h]==0:
                    swt+= doors[h]  
                    break""" 