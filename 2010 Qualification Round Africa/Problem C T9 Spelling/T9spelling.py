'''
Problem:
The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad. 
We would like to make it easier to write a message to your friend using a sequence of keypresses 
to indicate the desired characters. The letters are mapped onto the digits as shown below. 
To insert the character B for instance, the program would press 22. 
In order to insert two characters in sequence from the same key, 
the user must pause before pressing the key a second time. 
The space character ' ' should be printed to indicate a pause. 
For example, 2 2 indicates AA whereas 22 indicates B.
Source:
https://code.google.com/codejam/contest/351101/dashboard#s=p2
'''
file = open('T9smallInput.txt')
line = file.readlines()
file.close()

stuff = "x"

dict = {}
k = 2
i = -1
alpha = 'abcdefghijklmnopqrstuvwxyz'
for a in alpha:
    i+=1
    if (i == 3 and k != 7 and k != 9) or ((k == 7 or k == 9) and i == 4):
        k+=1
        i=0
    dict[a] = [k,i]
    
l = 1
for x in range(0, int(line[0])):
    print("Case #"+str(x+1)+": ",end="")
    word = line[l]
    prev = 0
    for w in word.rstrip('\n'):
        if w != ' ':  
            val = dict[w]
            if val[0] == prev:
                print(" ", end="")
            for g in range(0,val[1]+1):
                print(val[0],end="")
            prev = val[0]
        else:
            if prev == "0":
                print(" 0", end="")
            else:
                print("0", end="")
                prev = "0"
    print()
    l+=1