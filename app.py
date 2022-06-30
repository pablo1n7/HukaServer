from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def paint():
    return render_template('index.html')


@app.route('/setEspecies', methods=['POST'])
def especie():
    print('hola')