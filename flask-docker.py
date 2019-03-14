from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'v1.0.1'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
