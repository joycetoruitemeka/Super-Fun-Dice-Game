from random import randint

NUM_DICE = 3
DICE_SIDES = 6
MAX_SCORE = 50

def roll_dice():
    #Roll three dice and return the results as a list.
    return [randint(1, DICE_SIDES) for _ in range(NUM_DICE)]

def check_tuple_out(dice):
    #Check if all three dice have the same value
    return len(set(dice)) == 1

def fix_dice(dice):
    #Identify fixed and unfixed dice based on matching values
    fixed = [d for d in dice if dice.count(d) > 1]
    unfixed = [d for d in dice if dice.count(d) == 1]
    return fixed, unfixed

def player_turn(player_name):
    #Simulate a single player's turn
    print(f"\n{player_name}'s turn!")
    dice = roll_dice()
    print(f"Initial roll (as tuple): {tuple(dice)}")

    if check_tuple_out(dice):
        print("Tupled out! No points this turn.")
        return 0

    fixed, unfixed = fix_dice(dice)
    re_roll = True
    while re_roll:
        print(f"Fixed dice: {fixed}, Unfixed dice: {unfixed}")

        while True:
            choice = input("Re-roll unfixed dice? (yes/no): ").lower()
            if choice in ["yes", "no"]:
                break
            print("Invalid input! Please enter 'yes' or 'no'.")

        if choice != "yes":
            re_roll = False
        else:
            unfixed = [randint(1, DICE_SIDES) for _ in range(len(unfixed))]
            dice = fixed + unfixed
            print(f"New roll: {tuple(dice)}")
            if check_tuple_out(dice):
                print("Tupled out! No points this turn.")
                return 0
            fixed, unfixed = fix_dice(dice)

    score = sum(dice)
    print(f"{player_name} scores {score} points! Rolls {tuple(dice)}")
    return score

def print_scores(scores):
    #Print the current scores
    print("\nCurrent Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")

def game_loop():
    #Main game loop for managing player turns and determining the winner
    players = []
    num_players = 2
    for i in range(num_players):
        while True:
            name = input(f"Enter name for Player {i + 1}: ").strip()
            if name:
                players.append(name)
                break
            print("Name cannot be empty. Please enter a valid name.")

    scores = {player: 0 for player in players}
    max_score = MAX_SCORE

    while all(score < max_score for score in scores.values()):
        for player in players:
            print(f"\n{player}'s turn!")
            scores[player] += player_turn(player)
            print_scores(scores)

            if scores[player] >= max_score:
                print(f"{player} wins with {scores[player]} points!")
                return

# Start the game
game_loop()
