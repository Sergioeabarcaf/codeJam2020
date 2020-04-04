var count = window.prompt("Enter the number of use cases: ");

for(let i = 0; i < count; i++){
    let useCase, n = getUseCase();
    let trace = trace(useCase, n);
    let validColum = validColum(useCase, n);
    let validRow = validRow(useCase, n);
    x
}

function getUseCase() {
    let useCase = [];
    let n = window.prompt("Enter the size of the matriz: ");
    for(let i=0; i<n; i++){
        let row = [];
        for(let j=0; i<n ; j++){
            row.push(window.prompt(`Enter the number in position ${i},${j}`));
        }
        useCase.push(row);
    }
    return useCase, n;
}

function trace(useCase, size){
    let sum = 0;
    for(let i=0; i<size; i++){
        sum += useCase[i][i];
    }
    return sum;
}

function validColum(useCase, size){
    let acum = 0;
    for(let i=0; i<size; i++){
        acum += searchRepeated(useCase[i], size);
    }
    return acum;
}

function validRow(useCase, size){
    let acum = 0;
    let rowPosition = 0;
    while(rowPosition < size){
        let row = [];
        for(let i=0; i<size; i++){
            row.push(useCase[i,rowPosition]);
        }
        acum += searchRepeated(row, size);
        rowPosition += 1;
    }
    return acum;
}

function searchRepeated(array, size){
    for(let i=0; i<size; i++){
        for(let j=i+1; j<=size; j++){
            if(array[i] === array[j]){
                return 1;
            }
        }
    }
    return 0;
}