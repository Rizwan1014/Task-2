'''
Write a program that takes a string and returns True if it is a anagram of another string,False otherwise 
'''
# Data1 and Data2 are the two strings 
def are_anagram(data1, data2):
    clean_data1=''.join(char.lower() for char in data1 if char.isalnum())
    clean_data2=''.join(char.lower() for char in data2 if char.isalnum())
# compare the two string
    return sorted (clean_data1) == sorted(clean_data2)
# Input of the two string 
data1=input("Enter a string 1:")
data2=input("Enter a string 2:")
# checks whether its a anagram or not 
result=are_anagram(data1,data2)
print(result)
