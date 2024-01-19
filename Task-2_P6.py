'''
Write a program that takes a string and returns the longest common substring between them.
'''
def longest_common_substring(str1, str2):
    data1= len(str1)
    data2= len(str2)

    # Initialize a to store the length of common substrings
    table= [[0] * (data1 + 1) for _ in range(data2 + 1)]

    # Variables to store the length and end position of the longest common substring
    max_length = 0
    end_position = 0

    for i in range(1, data1 + 1):
        for j in range(1, data1 + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_position = i - 1
            else:
                table[i][j] = 0

    # Extract the longest common substring
    longest_common_sub = str1[end_position - max_length + 1: end_position + 1]

    return longest_common_sub

# Get input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Call the function and display the result
result = longest_common_substring(str1, str2)

if result:
    print(f"The longest common substring is: {result}")
else:
    print("There is no common substring.")
