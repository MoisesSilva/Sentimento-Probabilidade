import os
from flask import Flask, request
from flask_cors import CORS
import joblib as jb
import json

app = Flask(__name__)

model = jb.load("model-final3.pkl.z")

cors = CORS(app, resource={r'/*' : {"origins" : "*"}})

@app.route("/", methods=['GET'])
def index():
    print(request.args)

    mensagem = request.args.get("mensagem", default='')
    res = {"mensagem": mensagem, "p": model.predict_proba([mensagem])[0][1]}
    return json.dumps(res)

    #return "<h1>Olá, Heroku!!"

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

if __name__ == "__main__":
    main()