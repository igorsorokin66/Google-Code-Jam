'''
Problem:
After years of study, scientists at Google Labs have discovered an alien language transmitted from a faraway planet. 
The alien language is very unique in that every word consists of exactly L lowercase letters. 
Also, there are exactly D words in this language.

Once the dictionary of all the words in the alien language was built, 
the next breakthrough was to discover that the aliens have been transmitting messages to Earth for the past decade. 
Unfortunately, these signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. 
In order to help them decipher these messages, 
the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.

A pattern consists of exactly L tokens. 
Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). 
For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. 
Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.
Source:
https://code.google.com/codejam/contest/90101/dashboard#s=p0
'''
file = open('alienSmallInput.txt')
line = file.readlines()
file.close()

l = int(line[0].split()[0])
d = int(line[0].split()[1])
n = int(line[0].split()[2])

root = {}
for i in range(1,d+1):
    curr = root
    found = True
    for c in line[i].strip():
        if c in curr and found:
            curr = curr[c]
        else:
            found = False
            curr[c] = {}
            curr = curr[c]

count = 0
def compute(str,final,curr):
    if len(str) == 0:
        global count
        count+=1
    elif str[0] != '(':
        if str[0] in curr:
            compute(str[1:],final+str[0],curr[str[0]])
    else:
        for p in str[1:str.find(')')]:
            if len(final) < l and p in curr:
                compute(str[str.find(')')+1:len(str)],final+p,curr[p])

for i in range(d+1,d+1+n):
    compute(line[i].strip(),"",root)
    print("Case #"+str(i-d)+": ",end="")
    print(count)
    count = 0