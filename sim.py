import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

START_BALANCE = 10000
START_BET = 1
WIN_CHANCE = .5
PAYOFF_MULTIPLIER = 2
LOSS_MULTIPLIER = 0
ITERATIONS = 10000
MASS_RUN_TIMES = 1000

# Simplest working version of betting sim
def basic():
    balance = START_BALANCE
    balances = []
    for _ in range(ITERATIONS + 1):
        balances.append(balance)
        balance = one_iter(balances[-1])
    # visualize_bets(balances)
    return balances

# Logic for the increasing bet problem I am interested in
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
            break
        returned_money = one_iter(amount_at_stake)
        if returned_money > amount_at_stake:
            i = START_BET
        else:
            i *= 2
        balance = balance - amount_at_stake + returned_money
    
    # visualize_bets(balances)
    return balances
        
# One win or loss bet with balance resolution
def one_iter(money):
    result = random.choice([PAYOFF_MULTIPLIER, LOSS_MULTIPLIER])
    return money * result

# Runs the increasing bet logic many times and tracks data
def mass_run():
    log = []
    for _ in range(MASS_RUN_TIMES):
        balances = increasing_bet()
        # Log the final balance
        log.append(balances[-1])

    max_val = max(log)
    median_val = statistics.median(log)
    mode_val = statistics.mode(log)
    print(f"max: {max_val}, median: {median_val}, mode: {mode_val}")

    zero_occur = log.count(0)
    print(f"percent chance of losing everything is {(zero_occur / len(log)) * 100}")

    visualize_log(log)
    return log

# Graph of balance over time
def visualize_bets(balances):
    x = np.arange(0, len(balances))
    y = balances
    plt.plot(x, y)
    plt.show()

def visualize_log(log):
    plt.hist(log, bins=10, color="blue", edgecolor="black")
    plt.show()

if __name__ == "__main__":
    mass_run()