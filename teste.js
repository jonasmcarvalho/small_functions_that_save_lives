data = {
    nome: 'Jonas Carvalho',
    sobrenome: {
        primeiro_sobrenome: 'Marques',
        segundo_sobrenome: 'Carvalho',
        idade: '18',
        cidade: 'Ariranha',
    }
    
}


/* for (let key in data.sobrenome) {
    console.log(data.nome)
    console.log(data.sobrenome[key])
    console.log(key)
} */


let data1 = ['teste', 'um', 'teste2', 'ola']

for (let data of data1) {
    console.log(data)

}

for (let data in data1) {
    console.log(data1[data])

}