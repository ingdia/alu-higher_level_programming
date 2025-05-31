#!/usr/bin/node

let num1 = parseInt(process.argv[2])
let num2 = parseInt(process.argv[3])

if (isNaN(num1)|| isNaN(num2)){
    console.log(num1)
} else {
    function add(a,b){
    return a+b
    }
    console.log(add(num1, num2))
}


