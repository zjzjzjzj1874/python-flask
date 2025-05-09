from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# 请求钩子
@app.before_request
def before_request():
    print('before_request')
@app.after_request
def after_request(response):
    print('after_request')
    return response
@app.teardown_request
def teardown_request(exception):
    print('teardown_request')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/liveness', methods=['GET'])
def liveness():
    print('liveness check')
    return jsonify({"status": "ok"}), 200

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    print("request data ",data)
    return jsonify({"received":data}), 201

@app.route('/greet/<name>')
def greet(name):
    print(f'hello {name}!')
    return f'hello {name}!'

if __name__ == '__main__': 
    app.run(debug=True)