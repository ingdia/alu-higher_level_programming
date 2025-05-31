#!/usr/bin/node 

let x = process.argv[2];
x = parseInt(x);
let i = 0;
let word = "C is fun"
if(isNaN(x)){
    console.log('Missing number of occurrences');
} else {
    while( i < x ){
    console.log( word );
    i++
}
}

