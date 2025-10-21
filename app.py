from flask import Flask

appVictor = Flask(__name__)

@appVictor.route('/')
def raiz():
    return 'Olá, turma!'

if __name__ == '__main__':
    appVictor.run(debug=True)
