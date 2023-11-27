word = "Holberton"

# Update the variables to match the correct output
word_first_3 = word[0:3]
word_last_2 = word[-2:]
middle_index = len(word) // 2
middle_word = word[middle_index - 3:middle_index + 4]

# Print the updated results
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
