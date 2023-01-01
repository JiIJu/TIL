const products = [
    { name : 'a' , type : 've'},
    {name : 'b' , type : 'fr'},
    {name : 'c' , type : 've'},
    {name : 'd' , type : 'fr'},
]

// const fruitFilter = function (product) {
//     return product.type === 'fr'
// }

// const newArry = products.filter(fruitFilter)
// console.log(newArry)

// 2
// const newArry = products.filter(function (product) {
//     return product.type === 'fr'
// })

// 3

const newArry = products.filter( (product) => {
    return product.type === 'fr'
})
console.log(newArry)