from flask import Flask
from flask import render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def paint():
    return render_template('index.html')



@app.route('/setEspecies', methods=["POST", "GET"])
def especie():

    if request.method == "POST":
        json_dict = request.get_json()
        print(json_dict)
        data = {'resp': 'prueba',}
        return jsonify(data)
    else:

        return """<html><body>
        Something went horribly wrong
        </body></html>"""