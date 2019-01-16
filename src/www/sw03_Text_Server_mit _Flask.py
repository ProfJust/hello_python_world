### Simpler Flask Webserver
### Bsp aus https://www.youtube.com/watch?v=vyCboBjK4us 2:48
### sudo pip install flask

from flask import Flask

app = Flask(__name__)
@app.route("/")

def main():
    return "Welcome to the Flask Server !"

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port=80)