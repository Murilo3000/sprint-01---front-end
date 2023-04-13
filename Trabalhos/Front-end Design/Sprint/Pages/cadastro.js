var pergunta = prompt("Você possui uma conta conosco? s/n");
var usu = "usuário1"
var sen = "senha"
if (pergunta == "s"){
    var usuario = prompt("Digite o seu usuário: ")
    if (usuario == usu){
        var senha = prompt("Digite a sua senha")
        if (senha == sen){
            document.write("Bem vindo ao sistema!")
        } else {
            document.write("Não conseguimos localizar essa conta.")  
        }
    } else {
        document.write("Não conseguimos localizar essa conta.")
    }
} if (pergunta == "n"){
    var usuario = prompt("Digite o seu nome de usuário: ")
    var senha = prompt("Digite sua senha: ")
    alert("Faça o Login na página!")
    var usuario1 = prompt("Digite seu nome de usuário: ")
    if (usuario1 == usuario){
        var senha1 = prompt("Digite sua senha: ")
        if (senha1 == senha){
            document.write("Bem vindo ao sistema!")
        } else {
            document.write("Não conseguimos localizar essa conta.")  
        }
    } else {
        document.write("Não conseguimos localizar essa conta.")
    }
}
