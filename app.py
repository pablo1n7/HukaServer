from flask import Flask, url_for, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def paint():
    return render_template('index.html')


@app.route('/setEspecies', methods=['POST'])
def especie():
    print('hola')

if __name__=='__main__':
    app.run(debug=True)