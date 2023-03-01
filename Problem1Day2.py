f = open('C:\\Users\\Aniket\\Documents\\Advent of Code 2022\\inputProblem1Day2.txt', "r")
summation = 0
for count, line in enumerate(f):
    [m,n] = line.split()
    if(n == 'X'):
        summation =  summation + 1
    elif(n == 'Y'):
        summation = summation + 2
    elif(n == 'Z'):
        summation = summation + 3
    if m == 'A' and n == 'Y':
        summation = summation + 6
    elif m == 'A' and n == 'X':
        summation = summation + 3
    elif m == 'A' and n == 'Z':
        summation = summation + 0
    elif m == 'B' and n == 'X':
        summation = summation + 0
    elif m == 'B' and n == 'Y':
        summation = summation + 3
    elif m == 'B' and n == 'Z':
        summation = summation + 6
    elif m == 'C' and n == 'X':
        summation = summation + 6
    elif m == 'C' and n == 'Y':
        summation = summation + 0
    elif m == 'C' and n == 'Z':
        summation = summation + 3
print(summation)
