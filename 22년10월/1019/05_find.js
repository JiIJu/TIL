const avengers = [
    {name : 'hi',age:45},
    {name : 'Tony Stark' , age:32},
]

const avenger = avengers.find((avenger) => {
    return avenger.name === 'Tony Stark'
})

console.log(avenger)