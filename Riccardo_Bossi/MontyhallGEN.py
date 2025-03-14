import numpy as np
import random
import matplotlib.pyplot as plt

K = 10 #numero max di porte

prob_change = []
prob_no_change =[]

n = 10000

for N in range(3 , K+1): # N diventa il numero di porte in questo ciclo

    win_switch = 0  # Wins when switching doors
    win_no_switch = 0  # Wins without switching doors
    loss_switch = 0  # Losses when switching doors
    loss_no_switch = 0  # Losses without switching doors

    for i in range(n):

        doors = np.zeros(N) #array iniziale di tutte capre
        position = random.randint(0,N-1)  # Position of the prize 
        scelta = random.randint(0,N-1) # The door initially chosen by the player
        doors[position] = 1

        #print("doors: ", doors , "\n")

        s = 0 #numero di celle eliminate prima di scelta
        p = 0 #numero di celle eliminate prima di position

        #print("position:", position, "\n", "scelta:", scelta)

        M = random.randint(1,N-2)  #Number of doors open by the host, minimo 1
        #print("M: ", M, "\n")
        pos_to_del = set()

        while len(pos_to_del) < M:
            PosM = random.randint(0, N - 1)
            if doors[PosM] != 1 and PosM != scelta:
                pos_to_del.add(PosM)

        # Ordina le posizioni da eliminare
        pos_to_del = sorted(pos_to_del)

        # Correggo `s` e `p` 
        s = sum(1 for pos in pos_to_del if pos < scelta)
        p = sum(1 for pos in pos_to_del if pos < position)


        #print ("pos_to_del:" , pos_to_del , "\n")
        doors = np.delete(doors, list(pos_to_del))

        #print("doors2: ", doors , "\n")
        
        position = position - p #correggiamo le posizioni
        scelta = scelta - s
        
        #print("P" , p, "\n","S", s , "\n")

        #print("position 2 :", position, "\n", "scelta 2 :", scelta)

        change = random.randint(0,1) # 0 = doesn't switch, 1 = switches

        #print("change: ", change, "\n")

        #Player doesn't switch
        if scelta == position and change == 0 :
            win_no_switch += 1
        elif scelta != position and change == 0:
            loss_no_switch +=1
        
        #Player switch
        if scelta == position and change == 1 :
            loss_switch += 1
        elif scelta != position and change == 1 :
            while True : 
                a = random.randint(0, len(doors)-1)  # porta con cui sceglie di cambiare
                if a != scelta : #cioè non può scegliere la posizione precedente
                    break
            if position == a :
                win_switch += 1
            else :
                loss_switch += 1


    prob_no_switch =  win_no_switch / (win_no_switch + loss_no_switch)
    prob_switch = win_switch / (win_switch + loss_switch)

    print(f"Probability of winning without switch --> {N} doors: {prob_no_switch:.4f}")
    print(f"Probability of winning with switch --> {N} doors: {prob_switch:.4f} \n")

    prob_no_change.append(prob_no_switch)
    prob_change.append(prob_switch)

# Generazione degli istogrammi
plt.figure(figsize=(10, 5))

# Primo istogramma: Probabilità senza cambio
plt.subplot(1, 2, 1)
plt.bar(range(3, K + 1), prob_no_change, color='blue', alpha=0.7)
plt.title('Probabilità di vincita senza cambio')
plt.xlabel('Numero di porte (K)')
plt.ylabel('Probabilità')
plt.xticks(range(3, K + 1))

# Secondo istogramma: Probabilità con cambio
plt.subplot(1, 2, 2)
plt.bar(range(3, K + 1), prob_change, color='green', alpha=0.7)
plt.title('Probabilità di vincita con cambio')
plt.xlabel('Numero di porte (K)')
plt.ylabel('Probabilità')
plt.xticks(range(3, K + 1))

# Mostra gli istogrammi
plt.tight_layout()
plt.show()
