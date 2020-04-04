def getDataInt(message, min, max):
    while True:
        data = input(message)
        try:
            data = int(data)
            if(data <= max and data >= min):
                return data
            print('Number out range, try again')
        except:
            print('Only int data types are accepted')

def searchRepeated(array, size):
    for i in range(size):
        for j in range(i + 1,size):
            if(array[i] == array[j]):
                return 1
    return 0

def getUseCase():
    useCase = []
    size = getDataInt('Enter the size of the matriz (size between 2 and 100): ', 2, 100)
    for i in range(size):
        row = []
        for j in range(size):
            row.append(getDataInt('Enter the number in position ' + str(i) + ',' + str(j) + ' (number between 1 and ' + str(size) + '): ', 1, size))
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

count = getDataInt('Enter the number of use cases (use cases between 1 and 100): ', 1, 100)
for i in range(count):
    useCase, size = getUseCase()
    trace = getTrace(useCase, size)
    colum = validColum(useCase, size)
    row = validRow(useCase, size)
    print('Use case Nº ' + str(i))
    print('Trace: ' + str(trace))
    print('Colum: ' + str(colum))
    print('Row: ' + str(row))