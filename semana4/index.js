/*
Comentarios
*/

let mivariable;  // declarar variable
mivariable = "hola mundo"; // asignación de string

console.log(mivariable);

mivariable = 5; // reasignación a number

// Configuración de prompt-sync
const prompt = require('prompt-sync')({sigint: true}); // <-- Importa correctamente
const nombre = prompt("Ingrese su nombre: "); // <-- Usa la versión correcta

console.log(`El nombre de la persona es: ${nombre}`);
console.log("El nombre de la persona es: " + nombre);
console.log(typeof nombre);


//comparacion tipos de datos
// las igualdad ==
console.log(5 == "5"); // true, porque compara valor
console.log(5 === "5"); // false, porque compara valor y tipo
console.log(5 === 5); // true, porque son iguales en valor y tipo
console.log(true == 1); // true, es 1 como valor
console.log(true === true); // true, son iguales en valor y tipo

// las desigualdades !=
console.log(5 != "5"); // false, porque son iguales en valor
console.log(5 !== "5"); // true, porque son diferentes en tipo

// condicionales sentencia if
if (5 === "5") {
    console.log("Son iguales en valor y tipo");
} else if (5 == "5") {
    console.log("Son iguales en valor pero diferentes en tipo");
} else {
    console.log("Son diferentes en valor y tipo");
}

let count = 0;
while (count < 5) {
    console.log(`El valor de count es: ${count}`);
    count++; // count = count + 1
}

//tipos de datos primitivos
// string("", ), number, boolean, null, undefined, symbol

let name = "bruno"; // string
let edad = 25; // number
let esEstudiante = true; // boolean
let valorNulo = null; // null
let valorIndefinido; // undefined
let simbolo = Symbol("descripcion"); // symbol

