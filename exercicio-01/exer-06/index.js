(function () {

    'use script'
    console.log('Ola mundo');

    // 6 - Faça um programa que le uma quantidade de valores e calcula a media e a soma
    var soma = []
    var i = true
    var media;

    while (i == true) {
        var numeros = prompt("Digite um numero para começarmos e nao quando quiser sair: ")
        if (numeros == "nao") {
            break;
        }
        console.log(numeros)
        console.log(soma)
        console.log(soma.push(numeros))

    }

    var Myreduce = soma.reduce((acumulado, atual) => {
        return Number(acumulado) + Number(atual)
    })

    media = Myreduce / soma.length
    document.write(`A media é ${media}`)
    console.log(`A media é ${media}`)



})()