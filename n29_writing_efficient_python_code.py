# Gathering Pokémon without a loop
# A list containing 720 Pokémon has been loaded into your session as poke_names. Another list containing each Pokémon's corresponding generation has been loaded as poke_gens.

# A for loop has been created to filter the Pokémon that belong to generation one or two, and collect the number of letters in each Pokémon's name:

# gen1_gen2_name_lengths_loop = []

# for name,gen in zip(poke_names, poke_gens):
#     if gen < 3:
#         name_length = len(name)
#         poke_tuple = (name, name_length)
#         gen1_gen2_name_lengths_loop.append(poke_tuple)
# Instructions
# 100 XP
# Eliminate the above for loop using list comprehension and the map() function:

# Use list comprehension to collect each Pokémon that belongs to generation 1 or generation 2. Save this as gen1_gen2_pokemon.
# Use the map() function to collect the number of letters in each Pokémon's name within the gen1_gen2_pokemon list. Save this map object as name_lengths_map.
# Combine gen1_gen2_pokemon and name_length_map into a list called gen1_gen2_name_lengths.


# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])


# Pokémon totals and averages without a loop
# A list of 720 Pokémon has been loaded into your session called names. Each Pokémon's corresponding statistics has been loaded as a NumPy array called stats. Each row of stats corresponds to a Pokémon in names and each column represents an individual Pokémon stat (HP, Attack, Defense, Special Attack, Special Defense, and Speed respectively.)

# You want to gather each Pokémon's total stat value (i.e., the sum of each row in stats) and each Pokémon's average stat value (i.e., the mean of each row in stats) so that you find the strongest Pokémon.

# The below for loop was written to collect these values:

# poke_list = []

# for pokemon,row in zip(names, stats):
#     total_stats = np.sum(row)
#     avg_stats = np.mean(row)
#     poke_list.append((pokemon, total_stats, avg_stats))
# Instructions
# 0 XP
# Replace the above for loop using NumPy:
# Create a total stats array (total_stats_np) using the .sum() method and specifying the correct axis.
# Create an average stats array (avg_stats_np) using the .mean() method and specifying the correct axis.
# Create a final output list (poke_list_np) by combining the names list, the total_stats_np array, and the avg_stats_np array.

# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

# Error handling by raising an error
# Another way to raise an error is by using raise. In this exercise, you will add a raise statement to the shout_echo() function you defined before to raise an error message when the value supplied by the user to the echo argument is less than 0.

# The call to shout_echo() uses valid argument values. To test and see how the raise statement works, simply change the value for the echo argument to a negative value. Don't forget to change it back to valid values to move on to the next exercise!

# Instructions
# 100 XP
# Complete the if statement by checking if the value of echo is less than 0.
# In the body of the if statement, add a raise statement that raises a ValueError with message 'echo must be greater than or equal to 0' when the value supplied by the user to echo is less than 0.


# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)


# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Alice', 'David', 'Bob', 'Eve'],
    'Age': [25, 30, 25, 35, 30, 28]
}

df = pd.DataFrame(data)

# Find duplicates in the 'Name' column
duplicates = df['Name'].duplicated()

# Filter the DataFrame to show only rows with duplicates
duplicated_rows = df[duplicates]

print(duplicated_rows)



You can print all the columns in a Pandas DataFrame that are of numerical data type (integers or floating-point numbers) by selecting those columns and then printing their names. Here's how you can do it:

python
Copy code
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Height (inches)': [63.5, 70.2, 68.0],
    'Salary': [50000, 60000, 75000]
}

df = pd.DataFrame(data)

# Select numerical columns (int or float)
numerical_columns = df.select_dtypes(include=['int', 'float']).columns

# Print the names of numerical columns
for col in numerical_columns:
    print(col)