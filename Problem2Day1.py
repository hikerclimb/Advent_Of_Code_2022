f = open('C:\\Users\\Aniket\\Documents\\Advent of Code 2022\\inputProblem1Day1.txt', "r")
list = []
summation = 0
for count, line in enumerate(f):
    if line != '\n':
        summation += int(line)
    else:
        count = count + 1
        list.append(summation)
        summation = 0

print(sum(sorted(list ,reverse=True)[:3]))

