from flask import Flask
from flask import render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def paint():
    try:
        d = pd.read_csv('data.csv')
        return d.to_html()
    except:
        return render_template('index.html')



@app.route('/setEspecies', methods=["POST", "GET"])
def especie():

    if request.method == "POST":
        json_dict = request.get_json()
        print(json_dict)
        df = pd.DataFrame(json_dict)
        df.to_csv('data.csv', index=0)
        data = {'resp': 'prueba',}
        return jsonify(data)
    else:

        return """<html><body>
        Something went horribly wrong
        </body></html>"""