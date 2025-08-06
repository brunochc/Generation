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