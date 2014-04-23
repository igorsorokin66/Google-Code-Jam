'''
This solution, computes all possible combinations,
which takes too long to run.
'''
file = open('alienSmallInput.txt')
line = file.readlines()
file.close()

l = int(line[0].split()[0])
d = int(line[0].split()[1])
n = int(line[0].split()[2])

words = []
for i in range(1,d+1):
    words.append(line[i].strip())

count = 0
def compute(str,final):
    if len(str) == 0:
        if final in words:
            global count
            count+=1
    elif str[0] != '(':
        compute(str[1:],final+str[0])
    else:
        for p in str[1:str.find(')')]:
            if len(final) < l:
                compute(str[str.find(')')+1:len(str)],final+p)

for i in range(d+1,d+1+n):
    compute(line[i].strip(),"")
    print(count)
    count = 0
    