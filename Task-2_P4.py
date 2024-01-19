'''
Write a program that takes a string and returns the number of unique characters in it.
'''
def count_unique_characters(input_data):
    # Use a set to store unique characters
    unique_characters = set()

    # Iterate through each character in the input string
    for data in input_data:
        # Add the character to the set
        unique_characters.add(data)

    # Return the number of unique characters
    return len(unique_characters)

# Get input from the user
input_data = input("Enter a string: ")

# Call the function and display the result
result = count_unique_characters(input_data)
print(f"Number of unique characters: {result}")

