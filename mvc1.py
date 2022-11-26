from flask import Flask ,jsonify,request
from modelViewController import get_prediction

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Golden Eye"

@app.route("/predict-alphabet",methods=["POST"])
def predict_data():
    image = request.files.get("alphabet")
    predict=get_prediction(image)
    return jsonify({"prediction":predict}),200

if(__name__ == "__main__") :
    app.run(debug=True)   