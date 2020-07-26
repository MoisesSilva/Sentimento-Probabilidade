import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r'/*' : {"origins" : "*"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>Olá, Heroku!!"

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

if __name__ == "__main__":
    main()