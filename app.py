from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='text-align: center; font-size: 50px;'>Hello World, My name is Thinh!</h1>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80