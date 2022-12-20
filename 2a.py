# Initialize the total score
total_score = 0

# Read the input
with open('2in.txt', 'r') as f:
    for line in f:
        # Split the line into opponent and player shapes
        opponent_shape = line[0]
        player_shape = line[2]
        player_score = 0
        # Calculate the score for the round
        if player_shape == 'X':  # player plays Rock
            player_score = 1
            if opponent_shape == 'A':  #draw
                player_score += 3
        elif player_shape == 'Y':  # player plays Paper
            player_score = 2
            if opponent_shape == 'B':  #draw
                player_score += 3
        elif player_shape == 'Z':  # player plays Scissors
            player_score = 3
            if opponent_shape == 'C':  #draw
                player_score += 3

        if (player_shape == 'X' and opponent_shape == 'C') or \
             (player_shape == 'Y' and opponent_shape == 'A') or \
             (player_shape == 'Z' and opponent_shape == 'B'):  # win
            score = player_score + 6
        else:  # loss
            score = player_score + 0

        # Add the score for the round to the total score
        total_score += score

# Print the result
print(f'The total score is {total_score}.')