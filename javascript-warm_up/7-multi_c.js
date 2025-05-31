#!/usr/bin/node 

let x = process.argv[2];
x = parseInt(x);

if (isNaN(x)) {
    console.log('Missing number of occurrences');
} else {
    let i = 0;
    while( i < x ){
        console.log('C is fun');
        i++;
}
}

