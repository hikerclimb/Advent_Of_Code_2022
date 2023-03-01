def common_member(a,b):
    result = [i for i in a if i in b]
    return result[0]

def split_list(a_list):
    half = round(len(a_list)//2)
    #print(half)
    return a_list[:half], a_list[half:]


f = open('C:\\Users\\Aniket\\Documents\\Advent of Code 2022\\inputProblem1Day3.txt', "r")

summation = 0
for line in f:
    [A, B] = split_list(line)
    if common_member(A, B).islower() == True:
        summation = int(ord(common_member(A, B))) - 96 + summation
    else:
        summation = int(ord(common_member(A, B))) - 38 + summation
print(summation)

