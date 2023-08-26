from flask import Flask, render_template, request, jsonify
from code.api import API

app = Flask(__name__)
api = API()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    history = request.json['history']
    resp = api.request(history)
    return jsonify({'bot_response': resp})

if __name__ == '__main__':
    app.run(debug=True)