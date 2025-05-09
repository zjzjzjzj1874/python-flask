from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/liveness', methods=['GET'])
def liveness():
    return jsonify({"status": "ok"}), 200

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    return jsonify({"received":data}), 201

@app.route('/greet/<name>')
def greet(name):
    return f'hello {name}!'

if __name__ == '__main__': 
    app.run(debug=True)