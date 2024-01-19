'''
Write a program that takes a string and returns the number of words in it.
'''
# split the string into words
def count_words(input_data):
    words=input_data.split()
    #return the number of words 
    return len(words)
#get input from the user 
input_data=input("Enter a string:")
#call function and print the result 
result=count_words(input_data)
print(f"Number of words :{result}")
