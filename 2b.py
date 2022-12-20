# Initialize the total score
total_score = 0

# Read the input
with open('2in_test.txt', 'r') as f:
    for line in f:
        # Split the line into opponent and player shapes
        opponent_shape = line[0]
        player_shape = line[2]
        desired_outcome = line[2]

        # Calculate the score for the round
        if desired_outcome == 'X':  # player needs to lose
            if (opponent_shape == 'A' and player_shape == 'Z') or \
               (opponent_shape == 'B' and player_shape == 'X') or \
               (opponent_shape == 'C' and player_shape == 'Y'):  # player wins
                score = 6
            else:  # player loses
                score = 0
        elif desired_outcome == 'Y':  # player needs to draw
            if opponent_shape == 'A':  # player plays Rock
                score = 3
            elif opponent_shape == 'B':  # player plays Paper
                score = 3
            elif opponent_shape == 'C':  # player plays Scissors
                score = 3
        elif desired_outcome == 'Z':  # player needs to win
            if (opponent_shape == 'A' and player_shape == 'X') or \
               (opponent_shape == 'B' and player_shape == 'Y') or \
               (opponent_shape == 'C' and player_shape == 'Z'):  # player wins
                score = 6
            else:  # player loses
                score = 0

        # Add the score for the round to the total score
        total_score += score

# Print the result
print(f'The total score is {total_score}.')
'''

a/x = rock
b/y = paper
c/z = scissors

'''