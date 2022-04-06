def osa():
    w, h = 5, 5;
    Matrix = [[0 for x in range(w)] for y in range(h)]

    Matrix[0][1] = 6
    Matrix[0][3] = 1
    Matrix[1][3] = 2
    Matrix[1][4] = 2
    Matrix[1][2] = 5
    Matrix[2][4] = 5
    Matrix[3][4] = 1
    Matrix[4][2] = 5

    for i in range(w):
        for j in range(h):
            Matrix[j][i] = Matrix[i][j]
    for i in range(w):
        for j in range(h):
            if Matrix[i][j] == 0:
                Matrix[i][j] = 99

    laufliste = [["." for x in range(2)] for y in range(5)]
    return Matrix, laufliste


def wege(Matrix):
    posPath = []
    for j in range(5):
        for i in range(5):
            if 1 <= Matrix[i][j] < 99:
                tempor = ['{} -> {}'.format(j, i)]
                posPath.extend(tempor)
    return 'All possible ways:\n' + str(posPath)


def laufweg(laufliste):
    gesammtlist = []
    for index, item in enumerate(laufliste):
        zwischlist = []
        zwischlist.append(index)
        zwischzahl = item[1]
        jjj = True
        while jjj == True:
            if index == 0 and zwischzahl == 'Start':
                jjj = False
                zwischlist.append(0)
            else:
                for index_two, item_two in enumerate(laufliste):
                    if index_two == zwischzahl and item_two[1] != 'Start' and index_two != index:
                        zwischlist.append(zwischzahl)
                        zwischzahl = item_two[1]

                    elif index_two == zwischzahl and item_two[1] == 'Start' and index_two != index:
                        # zwischzahl = item_two[1]
                        # zwischlist.extend(zwischlist)
                        jjj = False
                        zwischlist.append(0)

                    else:
                        continue
        gesammtlist.append(zwischlist)
    print(gesammtlist)


def nextpoint(besucht, laufliste):  # if unbesucht
    temp = []
    for a, i in enumerate(laufliste):
        # print(a,i)
        if i[0] != '.' and a not in besucht:
            temp.append([a, i[0], i[1]])
        else:
            continue

    kurzweg = temp[0][1]
    kurzknoten = temp[0][0]
    # print(kurzweg, kurzknoten,sep="\t")
    for i in temp:  # to the shorter one
        if len(temp) >= 1:
            if kurzweg > i[1]:
                kurzweg = i[1]
                kurzknoten = i[0]
                value = kurzweg
                pointer = kurzknoten
            else:
                value = kurzweg
                pointer = kurzknoten
        elif len(temp) == 1:
            value = kurzweg
            pointer = kurzknoten
        else:
            continue
    return value, pointer


def grapha(Matrix, laufliste):
    besucht = []
    unbesucht = [0, 1, 2, 3, 4]
    value = 0
    pointer = 0

    while unbesucht:
        for i in range(len(Matrix)):
            if i in unbesucht:
                if Matrix[0][i] == 99 and pointer == 0:
                    laufliste[0][0] = value
                    laufliste[0][1] = 'Start'
                elif Matrix[pointer][i] != 99 and laufliste[i][0] != '.' and pointer != 0:
                    value += Matrix[pointer][i]
                    # print('neventuell new Value',value)
                    if laufliste[i][0] > value:
                        laufliste[i][0] = value
                        laufliste[i][1] = pointer
                        value -= Matrix[pointer][i]
                    else:
                        value -= Matrix[pointer][i]
                elif Matrix[pointer][i] != 99 and laufliste[i][0] == '.':
                    laufliste[i][0] = value + Matrix[pointer][i]
                    laufliste[i][1] = pointer
        unbesucht.remove(pointer)
        besucht.append(pointer)

        if unbesucht:
            value, pointer = nextpoint(besucht, laufliste)
            print('value:', value, 'pointer:', pointer)
        else:
            print('Final')
        print(laufliste)
        print(unbesucht)
        print(besucht)

    laufweg(laufliste)


Matrix, tabelle_weg = osa()
grapha(Matrix, tabelle_weg)
print(wege(Matrix))
