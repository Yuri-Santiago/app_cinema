function conteudo(id) {
    return fetch("http://127.0.0.1:5000/filme/" + id)
        .then(function (response) {
            return response.json(); // But parse it as JSON this time
        })
        .then(function (json) {
            let duracao = json.filme.duracao + " min"
            document.getElementById('titulo').innerHTML = json.filme.nome.toUpperCase()
            document.getElementById('faixaEtaria').innerHTML = json.filme.faixaEtaria
            document.getElementById('genero').innerHTML = json.filme.genero
            document.getElementById('duracao').innerHTML = duracao
            document.getElementById('diretor').innerHTML = json.filme.diretor.toUpperCase()
            document.getElementById('sinopse').innerHTML = json.filme.sinopse
            document.getElementById('capa').setAttribute(
                'src', 'data:image/jpeg;base64,' + json.filme.capa);
            document.getElementById('cartaz').setAttribute(
                'src', 'data:image/jpeg;base64,' + json.filme.cartaz);

            for (let i = 0; i < json.programacao.length; i++) {
                let semana = document.createElement("SPAN");
                let semanat = document.createTextNode("Dia: " + json.programacao[i].diaSemana + " | ");
                semana.appendChild(semanat);
                let hora = document.createElement("SPAN");
                let horat = document.createTextNode("Horário: " + json.programacao[i].diaHora + " | ");
                hora.appendChild(horat);
                let formato = document.createElement("SPAN");
                let formatot = document.createTextNode("Formato: " + json.programacao[i].formato + " | ");
                formato.appendChild(formatot);
                let idioma = document.createElement("SPAN");
                let idiomat = document.createTextNode("Idioma: " + json.programacao[i].idioma + " | ");
                idioma.appendChild(idiomat);
                let preco = document.createElement("SPAN");
                let precot = document.createTextNode("Preço: " + json.programacao[i].preco + "R$" + " | ");
                preco.appendChild(precot);
                let sala = document.createElement("SPAN");
                let salat = document.createTextNode("Sala: " + json.programacao[i].sala + " | ");
                sala.appendChild(salat);
                let quantidade = document.createElement("SPAN");
                let quantidadet = document.createTextNode("Quantidade Atual: " + json.programacao[i].quantidade);
                quantidade.appendChild(quantidadet);
                let para = document.createElement("P");
                para.appendChild(semana);
                para.appendChild(hora);
                para.appendChild(formato);
                para.appendChild(idioma);
                para.appendChild(preco);
                para.appendChild(sala);
                para.appendChild(quantidade);
                document.getElementById("sessions").appendChild(para);

            }
            for (let i = 0; i < json.elenco.length; i++) {
                let nomeAtor = document.createElement("SPAN");
                let nomeAtorT = document.createTextNode(" Ator: " + json.elenco[i].nome + " | ");
                nomeAtor.appendChild(nomeAtorT);
                let personagem = document.createElement("SPAN");
                let personagemT = document.createTextNode("Personagem: " + json.elenco[i].personagem);
                personagem.appendChild(personagemT);
                let paragrafo = document.getElementById("atores");
                let br = document.createElement('br');
                paragrafo.appendChild(nomeAtor);
                paragrafo.appendChild(personagem);
                paragrafo.appendChild(br);

            }
            console.log(json);
        })
}


const urlParams = new URLSearchParams(location.search);
if (urlParams.get('id') == null) {
    location.replace('index.html')
} else {
    conteudo(urlParams.get('id')).then(() => console.log('Tudo Certo'))
}