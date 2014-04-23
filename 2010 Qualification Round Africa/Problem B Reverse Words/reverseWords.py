'''
Problem:
Given a list of space separated words, reverse the order of the words. 
Each line of text contains L letters and W words. 
A line will only consist of letters and space characters. 
There will be exactly one space character between each pair of consecutive words.
Source:
https://code.google.com/codejam/contest/351101/dashboard#s=p1
'''
file = open('reverseSmallInput.txt')
line = file.readlines()
file.close()

l = 1
for x in range(0, int(line[0])):
    print("Case #"+str(x+1)+": ",end="")
    split = line[l].strip().split(" ")
    for s in range(len(split)-1,-1,-1):
        print(split[s]+" ",end="")
    print()
    l+=1