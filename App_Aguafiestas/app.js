document.querySelector("#switch").addEventListener('click', interruptor)

function interruptor(){
    document.querySelector("#rojo").style.display = 'none'
    document.querySelector("#verde").style.display = 'none'
    document.querySelector("#azul").style.display = 'none'
    document.querySelector("#amarillo").style.display = 'none'
    document.querySelector("#naranja").style.display = 'none'
}