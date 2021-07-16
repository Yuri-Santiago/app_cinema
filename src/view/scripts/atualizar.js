let cartaz = "";
let capa = "";

function transformarCartaz() {
    var file = document.querySelector(
        '#cartaz')['files'][0];

    var reader = new FileReader();
    console.log("next");

    reader.onload = function () {
        cartaz = reader.result.replace("data:", "")
            .replace(/^.+,/, "");

        cartazBase64 = cartaz;

        console.log(cartaz);
    }
    reader.readAsDataURL(file);
}

function transformarCapa() {
    var file = document.querySelector(
        '#capa')['files'][0];

    var reader = new FileReader();
    console.log("next");

    reader.onload = function () {
        capa = reader.result.replace("data:", "")
            .replace(/^.+,/, "");

        capaBase64 = capa;

        console.log(capa);
    }
    reader.readAsDataURL(file);
}

function fazPut(url, body) {
    fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('PUT response: ');
        console.log(text);
        location.reload()
    });
}

function atualizarFilme() {
    event.preventDefault()
    let id = document.getElementById("idFilme").value
    let url = "http://127.0.0.1:5000/filme/" + id
    let nome = document.getElementById("nome").value
    let sinopse = document.getElementById("sinopse").value
    let duracao = document.getElementById("duracao").value
    let genero = document.getElementById("genero").value
    let faixaEtaria = document.getElementById("faixaEtaria").value
    let distribuidora = document.getElementById("distribuidora").value
    let diretor = document.getElementById("diretor").value

    let body = {
        "nome": nome,
        "sinopse": sinopse,
        "duracao": duracao,
        "genero": genero,
        "faixaEtaria": faixaEtaria,
        "distribuidora": distribuidora,
        "diretor": diretor,
        "cartaz": cartaz,
        "capa": capa
    }

    fazPut(url, body)
}

function atualizarProgramacao() {
    event.preventDefault()
    let sala = document.getElementById("sala").value
    let url = "http://127.0.0.1:5000/programacao/" + sala
    let filme = document.getElementById("filmeProgramacao").value
    let diaHora = document.getElementById("diaHora").value
    let formato = document.getElementById("formato").value
    let idioma = document.getElementById("idioma").value
    let preco = document.getElementById("preco").value

    let body = {
        "filme": filme,
        "diaHora": diaHora,
        "formato": formato,
        "idioma": idioma,
        "preco": preco,
        "quantidade": 0
    }

    fazPut(url, body)
}

function atualizarAtor() {
    event.preventDefault()
    let url = "http://127.0.0.1:5000/elenco"
    let filme = document.getElementById("filmeAtor").value
    let nome = document.getElementById("nomeAtor").value
    let personagem = document.getElementById("personagem").value


    let body = {
        "filme": filme,
        "nome": nome,
        "personagem": personagem
    }

    fazPut(url, body)
}
