function conteudo(){
    return fetch("http://127.0.0.1:5000/filmes")
        .then(function (response) {
            return response.json(); // But parse it as JSON this time
        })
        .then(function (json) {
            let filme1 = json.filme.pop()
            let filme2 = json.filme.pop()
            let filme3 = json.filme.pop()
            let filme4 = json.filme.pop()
            let filme5 = json.filme.pop()

            document.getElementById('imgspot').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme1.capa);
            document.getElementById('spotlight').innerHTML = filme1.nome.toUpperCase()

            document.getElementById('filme1').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme1.cartaz);
            document.getElementById('filme2').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme2.cartaz);
            document.getElementById('filme3').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme3.cartaz);
            document.getElementById('filme4').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme4.cartaz);
            document.getElementById('filme5').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme5.cartaz);

            document.getElementById('link1').setAttribute(
                'href', 'film.html?id=' + filme1.id);
            document.getElementById('link2').setAttribute(
                'href', 'film.html?id=' + filme2.id);
            document.getElementById('link3').setAttribute(
                'href', 'film.html?id=' + filme3.id);
            document.getElementById('link4').setAttribute(
                'href', 'film.html?id=' + filme4.id);
            document.getElementById('link5').setAttribute(
                'href', 'film.html?id=' + filme5.id);

            console.log(json)
        })
}

function search(genero){
    return fetch("http://127.0.0.1:5000/filmes/" + decodeURIComponent(genero))
        .then(function (response) {
            return response.json(); // But parse it as JSON this time
        })
        .then(function (json) {
            window.alert('Número de Fimes Encontrados: ' + json.numero)
            let filme1 = json.filme.pop()
            let filme2 = json.filme.pop()
            let filme3 = json.filme.pop()
            let filme4 = json.filme.pop()
            let filme5 = json.filme.pop()

            document.getElementById('imgspot').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme1.capa);
            document.getElementById('spotlight').innerHTML = filme1.nome.toUpperCase()

            document.getElementById('filme1').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme1.cartaz);
            document.getElementById('link1').setAttribute(
                'href', 'film.html?id=' + filme1.id);
            document.getElementById('filme2').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme2.cartaz);
            document.getElementById('link2').setAttribute(
                'href', 'film.html?id=' + filme2.id);
            document.getElementById('filme3').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme3.cartaz);
            document.getElementById('link3').setAttribute(
                'href', 'film.html?id=' + filme3.id);
            document.getElementById('filme4').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme4.cartaz);
            document.getElementById('link4').setAttribute(
                'href', 'film.html?id=' + filme4.id);
            document.getElementById('filme5').setAttribute(
                'src', 'data:image/jpeg;base64,' + filme5.cartaz);
            document.getElementById('link5').setAttribute(
                'href', 'film.html?id=' + filme5.id);

            console.log(json)
        })
}
const urlParams = new URLSearchParams(location.search);
if (urlParams.get('genero') == null) {
    conteudo().then(() => console.log('Tudo Certo'))
} else {
    search(urlParams.get('genero')).then(() => console.log('Tudo Certo'))
}
