import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

START_BALANCE = 100
START_BET = 1
WIN_CHANCE = .5
PAYOFF_MULTIPLIER = 2
LOSS_MULTIPLIER = 0.5
ITERATIONS = 100

# Simplest working version of betting sim
def basic():
    balance = START_BALANCE
    balances = []
    for _ in range(ITERATIONS + 1):
        balances.append(balance)
        balance = one_iter(balances[-1])
    visualize(balances)

def increasing_bet():
    balance = START_BALANCE
    balances = []
    i = START_BET
    for _ in range(ITERATIONS + 1):
        balances.append(balance)
        if balance >= i:
            amount_at_stake = i
        elif balance >= START_BET:
            amount_at_stake = START_BET
        else:
            print("Out of money!")
            break
        returned_money = one_iter(amount_at_stake)
        if returned_money > amount_at_stake:
            i = START_BET
        else:
            i *= 2
        balance += returned_money
    
    visualize(balances)
        
# One win or loss bet with balance resolution
def one_iter(money):
    result = random.choice([PAYOFF_MULTIPLIER, LOSS_MULTIPLIER])
    return money * result

# Graph of balance over time
def visualize(balances):
    x = np.arange(0, len(balances))
    y = balances
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    increasing_bet()