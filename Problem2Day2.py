f = open('C:\\Users\\Aniket\\Documents\\Advent of Code 2022\\InputProblem1Day2.txt', "r")
summation = 0
for line in f:
    [m,n] = line.split()
    if m == 'A' and n == 'Y':
        summation = summation + 4
    elif m == 'B' and n == 'Y':
        summation = summation + 5
    elif m == 'C' and n == 'Y':
        summation = summation + 6
    elif m == 'A' and n == 'X':
        summation = summation + 3
    elif m == 'B' and n == 'X':
        summation = summation + 1
    elif m == 'C' and n == 'X':
        summation = summation + 2
    elif m == 'A' and n == 'Z':
        summation = summation + 8
    elif m == 'B' and n == 'Z':
        summation = summation + 9
    elif m == 'C' and n == 'Z':
        summation = summation + 7
print(summation)
