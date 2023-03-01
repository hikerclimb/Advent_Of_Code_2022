with open('C:\\Users\\Aniket\\Documents\\Advent of Code 2022\\inputProblem1Day4.txt', "r") as f:
    counter = 0

    for line in f:
        x, y = line.split(',')
        xstart, xend = x.split('-')
        ystart, yend = y.split('-')
        l1 = []
        l2 = []
        for x in set(range(int(xstart), int(xend) + 1)):
            l1.append(x)
        for y in set(range(int(ystart), int(yend) + 1)):
            l2.append(y)
        if len(l2) >= len(l1):
            if(set(l1).issubset(l2)):
                print('first','l1', l1[0], 'l2', l2[0])
                counter = counter + 1
        else:
            if(set(l2).issubset(l1)):
                print('second','l1', l1[0], 'l2', l2[0])
                counter = counter + 1
        
    print(counter)
