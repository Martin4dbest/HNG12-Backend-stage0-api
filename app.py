from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)  

@app.route('/', methods=['GET'])
def get_infomation():
    return jsonify({
        "email": "martinagoha7@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/Martin4dbest/HNG12-Backend-stage0-api"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
