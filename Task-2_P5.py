'''
Write a program that takes a string and returns True if its a Plaindrome ,False otherwise.
'''
def is_palindrome(input_data):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    data = ''.join(input_data.split()).lower()

    # Compare the original string with its reverse
    return data == data[::-1]

# Get input from the user
input_data = input("Enter a string: ")

# Call the function and display the result
result = is_palindrome(input_data)
if result:
    print("The given is a palindrome")
else:
    print("The given data is not a palindrome")
