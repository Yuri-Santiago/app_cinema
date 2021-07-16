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

function fazPost(url, body) {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('POST response: ');
        console.log(text);
        location.reload();
    });
}


function cadastrarFilme() {
    event.preventDefault()
    let url = "http://127.0.0.1:5000/filme"
    let nome = document.getElementById("nome").value
    let sinopse = document.getElementById("sinopse").value
    let duracao = document.getElementById("duracao").value
    let genero = document.getElementById("genero").value
    let faixaEtaria = document.getElementById("faixaEtaria").value
    let distribuidora = document.getElementById("distribuidora").value
    let diretor = document.getElementById("diretor").value
    let body = {
        "nome": decodeURI(nome),
        "sinopse": sinopse,
        "duracao": duracao,
        "genero": genero,
        "faixaEtaria": faixaEtaria,
        "distribuidora": distribuidora,
        "diretor": diretor,
        "cartaz": cartaz,
        "capa": capa
    }

    fazPost(url, body)
}

function cadastrarProgramacao() {
    event.preventDefault()
    let url = "http://127.0.0.1:5000/programacao"
    let filme = document.getElementById("filmeProgramacao").value
    let diaHora = document.getElementById("diaHora").value
    let diaSemana = document.getElementById("diaSemana").value
    let sala = document.getElementById("sala").value
    let formato = document.getElementById("formato").value
    let idioma = document.getElementById("idioma").value
    let preco = document.getElementById("preco").value


    let body = {
        "filme": filme,
        "diaHora": diaHora,
        "diaSemana": diaSemana,
        "sala": sala,
        "formato": formato,
        "idioma": idioma,
        "preco": preco,
        "quantidade": 0
    }

    fazPost(url, body)
}

function cadastrarAtor() {
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

    fazPost(url, body)
}
