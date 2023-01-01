const arr = [1,2,3,4,5]

// 1
// const result = arr.find(function (elem) {
//     return elem % 2 === 0
// })
// 2
// const result = arr.find((elem) => {
//     return elem % 2 === 0
// })

// 4
const result = arr.every((elem) => elem%2 === 0)

console.log(result)