from flask import Flask, render_template

appVictor = Flask(__name__, template_folder= "templates")

@appVictor.route("/")  
def homepage():
    return render_template ("homepage.html")

if __name__ == '__main__':
    appVictor.run(port = 8000, debug = True)
