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

// Declaración de variables con var, let y const
var variableVar = "Soy var"; // var tiene alcance de función
let variableLet = "Soy let"; // let tiene alcance de bloque
const variableConst = "Soy const"; // const no puede ser reasignada

console.log(variableVar);
console.log(variableLet);
console.log(variableConst);

// Operadores básicos
let suma = 2 + 3; // suma
let resta = 5 - 2; // resta
let multiplicacion = 3 * 4; // multiplicación
let division = 10 / 2; // división
let concatenacion = "Hola" + " " + "Mundo"; // concatenación de strings

console.log("Suma:", suma);
console.log("Resta:", resta);
console.log("Multiplicación:", multiplicacion);
console.log("División:", division);
console.log("Concatenación:", concatenacion);

// Funciones
function saludar(nombre) {
    return "Hola, " + nombre + "!";
}
console.log(saludar("Bruno"));

// Arrays
let frutas = ["manzana", "banana", "naranja"];
console.log("Frutas:", frutas);
console.log("Primera fruta:", frutas[0]);

// Objetos
let persona = {
    nombre: "Bruno",
    edad: 25,
    esEstudiante: true
};
console.log("Persona:", persona);
console.log("Nombre de la persona:", persona.nombre);

// Bucle for
for (let i = 0; i < 3; i++) {
    console.log("El valor de i es:", i);
}

// Comentarios en JavaScript
// Esto es un comentario de línea

/*
Esto es un comentario
de bloque
*/

