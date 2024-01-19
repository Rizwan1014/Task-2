'''
Write a program that takes a string and returns a new string with all the vowels removed.
'''
#input the string
input_data="Welcome to Chennai"
result=input_data # storing the values
vowels=('a','e','i','o','u','A','E','I','O','U')
# itreating the string to check the vowels to remove 
for data in input_data.lower():
    if data in vowels:
        result=result.replace(data, "")
# printing after removing the vowels from the string 
print("After removing vowels:",result)
