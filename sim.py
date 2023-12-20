import random
import statistics
import matplotlib as plt

START_BALANCE = 100
WIN_CHANCE = .5
PAYOFF_MULTIPLIER = 2
LOSS_MULTIPLIER = 0.5
ITERATIONS = 10

def main():
    balance = START_BALANCE
    balances = [balance]
    for _ in range(ITERATIONS):
        new_balance = one_iter(balances[-1])
        balances.append(new_balance)

def one_iter(balance):
    result = random.choice([PAYOFF_MULTIPLIER, LOSS_MULTIPLIER])
    return balance * result

def visualize(balances):
    fig, ax = plt.subplots()
    
    ax.plot([i for i in range(len(balances))], [balances])

if __name__ == "__main__":
    main()