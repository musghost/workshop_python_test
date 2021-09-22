from flask import Flask

app = Flask(__name__)

@app.route("/some_user")
def hello_world():
    return {
        "age": 3,
        "name": "John",
        "account": {
            "enabled": False
        }
    }

    age = cs.process_age()
