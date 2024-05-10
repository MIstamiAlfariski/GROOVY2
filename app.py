from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("index.html")


@app.post("/get")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    responses = get_response(text)
    message = {"answer": responses}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
