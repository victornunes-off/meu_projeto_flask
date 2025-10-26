from flask import Flask, render_template

appVictor = Flask(__name__, template_folder= "templates")

@appVictor.route("/")  
def homepage():
    return render_template ("homepage.html")

@appVictor.route("/contato")
def contato():
    return render_template("contato.html")

@appVictor.route('/usuario')
def dados_usuarios():
    dados_usu = {"nome": "Victor", "profissao": "Programador", "empresa": "FCR"}
    return render_template ("usuario.html", dados =dados_usu) 

if __name__ == '__main__':
    appVictor.run(port = 8000, debug = True)
