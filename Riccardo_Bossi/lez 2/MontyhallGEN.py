import numpy as np
import random
import matplotlib.pyplot as plt
import statistics as statistic

K = 10  # Max number of doors

prob_change = []
prob_no_change = []
prob_mean_newcome = []
formula_values = []  # Lista per i valori teorici

n = 10000  # Number of iterations

for N in range(3, K + 1):  # N = number of doors in each cycle

    win_switch = 0  # Wins when switching doors
    win_no_switch = 0  # Wins without switching doors
    loss_switch = 0  # Losses when switching doors
    loss_no_switch = 0  # Losses without switching doors

    prob_newcome = []  # Probabilities for the newcome

    for i in range(n):

        doors = np.zeros(N)  # Initial array of goats
        position = random.randint(0, N - 1)  # Position of the prize
        scelta = random.randint(0, N - 1)  # The door initially chosen by the player
        doors[position] = 1  # Put the prize back behind one of the doors

        s = 0  # Number of cells deleted before the chosen door
        p = 0  # Number of cells deleted before the position

        M = N - 2  # Number of doors opened by the host
        #puoi modificare qui il programma per il numero di porte aperte

        prob_newcome.append(1 / (N - M))  # Probability for the newcomer

        pos_to_del = set()  # Set of open doors

        while len(pos_to_del) < M:
            PosM = random.randint(0, N - 1)
            if doors[PosM] != 1 and PosM != scelta:
                pos_to_del.add(PosM)

        pos_to_del = sorted(pos_to_del)  # Sorting the array

        # Calculate corrections for s and p
        s = sum(1 for pos in pos_to_del if pos < scelta)
        p = sum(1 for pos in pos_to_del if pos < position)

        doors = np.delete(doors, list(pos_to_del))  # Opening of the doors

        position = position - p  # Correction for position and scelta
        scelta = scelta - s

        change = random.randint(0, 1)  # 0 = doesn't switch, 1 = switches

        # Player doesn't switch
        if scelta == position and change == 0:
            win_no_switch += 1
        elif scelta != position and change == 0:
            loss_no_switch += 1

        # Player switches
        if scelta == position and change == 1:
            loss_switch += 1
        elif scelta != position and change == 1:
            while True:
                a = random.randint(0, len(doors) - 1)  # Doors where the player can change
                if a != scelta:  # Can't choose the previous door
                    break
            if position == a:
                win_switch += 1
            else:
                loss_switch += 1

    prob_no_switch = win_no_switch / (win_no_switch + loss_no_switch)
    prob_switch = win_switch / (win_switch + loss_switch)

    print(f"Probability of winning without switch --> {N} doors: {prob_no_switch:.4f}")
    print(f"Probability of winning with switch --> {N} doors: {prob_switch:.4f}")
    print(f"Probability of winning for the newcomer --> {N} doors: {statistic.mean(prob_newcome):.4f} \n")

    prob_no_change.append(prob_no_switch)
    prob_change.append(prob_switch)
    prob_mean_newcome.append(statistic.mean(prob_newcome))

    # Formula for the theoretical probability based on N and M
    formula_values.append((1 / N) * (N - 1) / (N - 1 - M))  # Theoretical formula

# Generating histograms
plt.figure(figsize=(15, 5))

# First histogram: Probability without change
plt.subplot(1, 3, 1)
plt.bar(range(3, K + 1), prob_no_change, color='blue', alpha=0.7)
plt.title('Probabilità di vincita senza cambio')
plt.xlabel('Numero di porte (K)')
plt.ylabel('Probabilità')
plt.xticks(range(3, K + 1))

# Second histogram: Probability with change
plt.subplot(1, 3, 2)
plt.bar(range(3, K + 1), prob_change, color='green', alpha=0.7)
plt.title('Probabilità di vincita con cambio')
plt.xlabel('Numero di porte (K)')
plt.ylabel('Probabilità')
plt.xticks(range(3, K + 1))

# Add theoretical points to the second histogram
plt.plot(range(3, K + 1), formula_values, 'o', color='red', label='Valori da formula')

# Third histogram: Probability for the newcomer
plt.subplot(1, 3, 3)
plt.bar(range(3, K + 1), prob_mean_newcome, color='red', alpha=0.7)
plt.title('Probabilità di vincita nuovo arrivato')
plt.xlabel('Numero di porte (K)')
plt.ylabel('Probabilità')
plt.xticks(range(3, K + 1))

# Show the histograms
plt.tight_layout()
plt.show()
