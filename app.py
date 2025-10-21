from flask import Flask

appVictor = Flask(__name__)

@appVictor.route('/')
@appVictor.route('/ola')
def raiz():
    return 'Olá, professora!'

def saudacoes (nome):
    return f'Olá, {nome}!'

if __name__ == '__main__':
    appVictor.run(port = 8000)
