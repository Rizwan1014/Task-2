'''
Write a pyramid of Numbers from 1 to 20 using For loop ?
'''
# i as variable itearate until the condition satisfies
for i in range (1,21):
    print (""*(21-i),end ="")
    # j as variabe
    for j in range(1,i+1):
        print(j,end="")
    print()