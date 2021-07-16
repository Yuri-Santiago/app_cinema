function fazDelete(url, body) {
    fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('DELETE response: ');
        console.log(text);
        location.reload()
    });
}

function deletarFilme() {
    event.preventDefault()
    let url = "http://127.0.0.1:5000/filme"
    let nome = document.getElementById("nome").value

    let body = {
        "nome": nome
    }
    fazDelete(url, body)
}

function deletarProgramacao() {
    event.preventDefault()
    let url = "http://127.0.0.1:5000/programacao"
    let sala = document.getElementById("sala").value
    let filme = document.getElementById("filmeProgramacao").value
    let diaHora = document.getElementById("diaHora").value

    let body = {
        "sala": sala,
        "filme": filme,
        "diaHora": diaHora,
    }

    fazDelete(url, body)
}

function atualizarAtor() {
    event.preventDefault()
    let url = "http://127.0.0.1:5000/elenco"
    let filme = document.getElementById("filmeAtor").value
    let nome = document.getElementById("nomeAtor").value


    let body = {
        "filme": filme,
        "nome": nome,
    }

    fazDelete(url, body)
}