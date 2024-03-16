let fs = require("fs")

// Intitializing the readFileLines with the file
const readFileLines = filename =>
   fs.readFileSync(filename)
   .toString('UTF8')

// Calling the readFiles function with file name
let arr = readFileLines("D:\\pragatheeshwar\\Smart India Hack\\coco.names.txt");
arr = arr.split("\n")
// Printing the response array
console.log(arr[1]);