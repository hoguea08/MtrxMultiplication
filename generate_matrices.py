def generate_XT():
    '''
    generates a matrix XT

    :return: returns a list containing the XT matrix
    '''
    XT = [[0 for i in range(2)] for j in range(11)]

    for i in range(11):
        for j in range(2):
            if j == 0:
                XT[i][j] = 1
            else:
                XT[i][j] = i
    return XT


def generate_X():
    '''
    generates the X matrix

    :return: returns a list containing the X matrix
    '''
    X = [[0 for i in range(11)] for j in range(2)]

    for i in range(11):
        for j in range(2):
            if j == 0:
                X[j][i] = 1
            else:
                X[j][i] = i
    return X


def generate_Y():
    '''
    generates the Y matrix

    :return: returns a list containing the Y matrix
    '''
    Y = [[0 for i in range(11)] for j in range(1)]

    for i in range(len(Y)):
        for j in range(len(Y[0])):
            Y[i][j] = j * j
    return Y
