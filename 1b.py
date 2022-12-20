# Initialize a list to store the total Calories for each Elf
elf_calories = [0]

# Initialize a variable to keep track of the current Elf
current_elf = 0

# Read the input
with open('1in.txt', 'r') as f:
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

# Sort the elf_calories list in descending order
elf_calories.sort(reverse=True)

# Calculate the total Calories carried by the top three Elves
top_three_calories = sum(elf_calories[:3])

# Print the result
print(
    f'The top three Elves are carrying {top_three_calories} Calories in total.'
)
