from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return b"Hello! This is a simple Flask application running inside Docker.NoYaaaaaaa"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    