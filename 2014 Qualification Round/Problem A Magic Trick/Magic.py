'''
Problem:
The magician starts by arranging 16 cards in a square grid: 
4 rows of cards, with 4 cards in each row. 
Each card has a different number from 1 to 16 written on the side that is showing. 
Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.

Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. 
Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, 
the magician then correctly determines which card the volunteer chose. Amazing, right?

You decide to write a program to help you understand the magician's technique. 
The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: 
the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. 
The rows are numbered 1 to 4 from top to bottom.

Your program should determine which card the volunteer chose; 
or if there is more than one card the volunteer might have chosen (the magician did a bad job); 
or if there's no card consistent with the volunteer's answers (the volunteer cheated).

Source:
https://code.google.com/codejam/contest/2974486/dashboard
'''

file = open('magicRealInput.txt')
line = file.readlines()
file.close()
l = 1
for x in range(0, int(line[0])):
    posA = int(line[l].strip())
    a = []
    for i in range(1,5):
        if i == posA:
            a = line[l+i].strip().split(" ")
    l+= 5
    posB = int(line[l].strip())
    b = []
    for i in range(1,5):
        if i == posB:
            b = line[l+i].strip().split(" ")
    l+= 5
    result = list(set(a)&set(b))
    print("Case #"+str(x+1)+": ",end="")
    if len(result) == 1:
        print(result[0])
    elif len(result) > 1:
        print("Bad magician!")
    else:
        print("Volunteer cheated!")