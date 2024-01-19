'''
Write a python program to calculate the total number of Vowels and Count ecah individual vowel A,E,I,O,U in the string "Guvi Network Private Limited" ?
'''

data ="Guvi Geeks Network Private Limited "
count =0

# iterate over the string
for data in data:
    if data=='a' or data=='e'or data=='i' or data=='o' or data=='u':
        count = count+1

#print the total vowels in a string
print("Number of vowels in the string :",count)
