// const myInfo = {
//     name : 'jack',
//     phoneNumber : '123456',
//     'samsung product' : {
//         buds : 'Buds Pro',
//         galaxy : 'S99',
//     },
// }

// console.log(myInfo['name'])
// console.log(myInfo['samsung product'].galaxy)

// const obj = {
//     name : 'jack',
//     greeting() {
//         console.log('hi!')
//     }
// }
// console.log(obj.name)
// console.log(obj.greeting())

const jsonData = {
    coffee : 'Americano',
    iceCreame : 'Mint Choco',

}
// console.log(jsonData)
// Object >> json
const objToJson = JSON.stringify(jsonData)
console.log(objToJson)
// json >> object
const JsonToobj = JSON.parse(objToJson)
console.log(JsonToobj)
