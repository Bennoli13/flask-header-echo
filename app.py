from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def echo_headers():
    headers = dict(request.headers)
    print("Received Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")
    return jsonify(headers), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
