def getDataInt(message):
    data = int(input(message))
    return data

def searchRepeated(array, size):
    for i in range(size):
        for j in range(i + 1,size):
            if(array[i] == array[j]):
                return 1
    return 0

def getUseCase():
    useCase = []
    size = getDataInt('Enter the size of the matriz: ')
    for i in range(size):
        row = []
        for j in range(size):
            row.append(getDataInt('Enter the number in position ' + str(i) + ',' + str(j) + ': '))
        useCase.append(row)
    return useCase, size

def getTrace(useCase, size):
    sum = 0
    for i in range(size):
        sum += useCase[i][i]
    return sum

def validColum(useCase, size):
    acum = 0
    for i in range(size):
        acum += searchRepeated(useCase[i], size)
    return acum

def validRow(useCase, size):
    acum = 0
    rowPosition = 0
    while(rowPosition < size):
        row = []
        for i in range(size):
            row.append(useCase[i][rowPosition])
        acum += searchRepeated(row, size)
        rowPosition += 1
    return acum

count = getDataInt('Enter the number of use cases: ')
for i in range(count):
    useCase, size = getUseCase()
    trace = getTrace(useCase, size)
    colum = validColum(useCase, size)
    row = validRow(useCase, size)
    print('Use case Nº ' + str(i))
    print('Trace: ' + str(trace))
    print('Colum: ' + str(colum))
    print('Row: ' + str(row))