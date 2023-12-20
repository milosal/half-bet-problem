import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

START_BALANCE = 100
WIN_CHANCE = .5
PAYOFF_MULTIPLIER = 2
LOSS_MULTIPLIER = 0.5
ITERATIONS = 10

def main():
    balance = START_BALANCE
    balances = []
    for _ in range(ITERATIONS + 1):
        balances.append(balance)
        balance = one_iter(balances[-1])
    visualize(balances)

def one_iter(balance):
    result = random.choice([PAYOFF_MULTIPLIER, LOSS_MULTIPLIER])
    return balance * result

def visualize(balances):
    x = np.arange(0, ITERATIONS + 1)
    y = balances
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()