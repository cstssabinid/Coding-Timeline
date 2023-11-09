import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_craps():
    point = roll_dice()
    if point in (2, 3, 12):
        return False
    elif point in (7, 11):
        return True

    while True:
        current_roll = roll_dice()
        if current_roll == point:
            return True
        elif current_roll == 7:
            return False

def simulate_craps_games(num_games):
    wins = 0
    for _ in range(num_games):
        if play_craps():
            wins += 1
    return wins

if __name__ == "__main__":
    num_simulations = 1000000
    num_wins = simulate_craps_games(num_simulations)
    win_probability = num_wins / num_simulations
    print(f"Number of simulations: {num_simulations}")
    print(f"Number of wins: {num_wins}")
    print(f"Win probability: {win_probability:.6f}")