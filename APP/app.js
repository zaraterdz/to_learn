document.querySelector('#buscador').addEventListener('click', funcionChingona)

function funcionChingona(){

    const day = document.querySelector('#buscador').value

    if(day === "lunes" || day === "martes" || day === "miercoles" || day === "jueves" || day === "viernes"){
        console.log("TIENES CLASES!")
    }
    else if(day === "sabado" || day === "domingo"){
        console.log("FIN DE SEMANA!")
    }
    else{
        console.log("ABURRIDO")
    }
}