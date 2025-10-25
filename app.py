from flask import Flask

appVictor = Flask(__name__)

@appVictor.route('/')
@appVictor.route('/rota1')
def raiz():
    return 'Olá, professora!'

@appVictor.route('/rota2')
def rota2():
    resposta = "<H3> Página da rota 2 <H3>"
    return resposta

def saudacoes (nome):
    return f'Olá, {nome}!'

if __name__ == '__main__':
    appVictor.run(port = 8000)
