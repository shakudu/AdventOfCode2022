# Initialize a list to store the total Calories for each Elf
elf_calories = [0]

# Initialize a variable to keep track of the current Elf
current_elf = 0

# Read the input
with open('input.txt', 'r') as f:
    for line in f:
        # Check if the line is a blank line
        if line.strip() == '':
            # If it is, move on to the next Elf
            current_elf += 1
            # Increase the size of the elf_calories list if necessary
            if current_elf >= len(elf_calories):
                elf_calories.append(0)
        else:
            # If it is not, parse the caloric value and add it to the current Elf's total
            calories = int(line.strip())
            elf_calories[current_elf] += calories

# Find the Elf with the highest total Calories
max_elf = 0
max_calories = 0
for i, calories in enumerate(elf_calories):
    if calories > max_calories:
        max_elf = i + 1
        max_calories = calories

# Print the result
print(
    f'Elf {max_elf} is carrying the most Calories, with a total of {max_calories}.'
)
