from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': 'Testing Akash Network!',
        'service': 'Python Lambda-style API'
    })

@app.route('/invoke', methods=['POST'])
def invoke():
    data = request.get_json() or {}
    return jsonify({
        'statusCode': 200,
        'body': f"Processed: {data}",
        'executedOn': 'Akash Network'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)