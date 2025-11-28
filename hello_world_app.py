from flask import Flask

# Прростое Flask приложение, возвращающее "Hello World!"
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
