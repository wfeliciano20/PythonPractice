import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
# set the first player as the winner
winner = players[0]
# set the amount of correct numbers from the lottery
winner_match = len(players[0]['numbers'].intersection(lottery_numbers))

for player in players:  # Go over each player
    # Calculate how many numbers they matched
    matched_numbers = len(player['numbers'].intersection(lottery_numbers))
    # If they matched more than the current top player...
    if matched_numbers > winner_match:
        top_player = player  # Say this player is the new top player
        winner_match = matched_numbers

# Calculate their winnings using the formula!
winnings = 100 ** winner_match

# Then print out—here in Udemy we have to use .format, but normally you'd want to use f-strings.
print('{} won {}.'.format(top_player['name'], winnings))
