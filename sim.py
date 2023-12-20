import random
import statistics
import matplotlib

START_BALANCE = 100
WIN_CHANCE = .5

def main():
    balance = START_BALANCE
    balances = [balance]
    for _ in range(10):
        new_balance = one_iter(balances[-1])
        balances.append(new_balance)


def one_iter(balance):
    pass

def visualize(balances):
    pass

if __name__ == "__main__":
    main()