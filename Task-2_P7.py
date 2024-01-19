'''
Write a program that takes a string and returns the most frequent characters in it.
'''
#Input the string 
input_data= "Hello World"
print ("The string is : ",input_data)

max_frequency = {}
#Iterate through each character in a string 
for data in input_data:
   if data in max_frequency:
      max_frequency[data] += 1
   else:
      max_frequency[data] = 1
result = max(max_frequency, key = max_frequency.get)
# Displaying the most frequent character
print ("The most frequent character is  : ",result)