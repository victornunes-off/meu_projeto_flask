from flask import Flask, render_template
from flask import request
from flask import flash
from flask import redirect

appVictor = Flask(__name__, template_folder= "templates")

@appVictor.route("/")  
@appVictor.route("/index")  
def indice():
    return render_template ("index.html")

@appVictor.route("/contato")
def contato():
    return render_template("contato.html")

@appVictor.route("/login")
def login():
    return render_template("login-auth.html")

@appVictor.route("/usuario/<nome>;<profissao>")
@appVictor.route("/usuario", defaults={"nome":"usuário?","profissao":""}) 
def usuarios (nome, profissao):
    dados_usu = {"profissao": profissao, "empresa":"FCR"}
    return render_template ("usuario.html", nome = nome, dados = dados_usu)  

# @appVictor.route('/usuario')
# def dados_usuarios():
#     dados_usu = {"nome": "Victor", "profissao": "Programador", "empresa": "FCR"}
#     return render_template ("usuario.html", dados =dados_usu)

# @appVictor.route("/usuario/<nome>;<profissao>;<empresa>") 
# def usuario (nome, profissao, empresa):    
#     dados_usu = {"profissao": profissao, "empresa": empresa}
#     return render_template ("usuario.html", nome = nome, dados = dados_usu)

@appVictor.route("/autenticar", methods=['GET','POST']) 
def autenticar():
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    if verificar_login(usuario, senha):
        msg = "Login e senha corretos. Acesso permitido."
        return f"{msg} para {usuario} "
    else:
        flash("Dados inválidos!")
        flash("Login ou senha incorretos. Acesso negado.")
        return redirect ('/login')

tabelaUsuarios = {
    "victor": "SuperSenh@2000",
    "alunoIFRO": "SuperSenh@2000",
    "visitante": "SuperSenh@2000"
}

def verificar_login(login, senha):
    if login in tabelaUsuarios and tabelaUsuarios[login] == senha:
        return True
    else:
        return False

@appVictor.route("/novocadastro/<nome_usuario>" , methods=['POST'])
@appVictor.route("/novocadastro/", defaults={"nome_usuario":""} , methods=['POST'])
def cadastroUsuario(nome_usuario):
    nome_usuario = request.form.get('nome_usuario')
    return render_template("cadastro.html", nome_login = nome_usuario )

if __name__ == '__main__':
    appVictor.run(port = 8000)
