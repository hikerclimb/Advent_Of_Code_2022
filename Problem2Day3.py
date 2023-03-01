def common_member(a,b,c):
    result = [i for i in a if i in b and i in c]
    return result[0]

f = open('C:\\Users\\Aniket\\Documents\\Advent of Code 2022\\inputProblem2Day3.txt', "r")
a = ""
b = ""
c = ""

commonLetter = []
for count, line in enumerate(f):
    summation = 0
    if count % 3 == 0:
        a = line
    elif count % 3 == 1:
        b = line
    elif count % 3 == 2:
        c = line
        commonLetter.append(common_member(a,b,c))

for i in commonLetter:
    print(i)
    if i.islower() == True:
        summation = int(ord(i)) - 96 + summation
    else:
        summation = int(ord(i)) - 38 + summation
print(summation)
