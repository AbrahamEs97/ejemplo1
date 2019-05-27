from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():

    return "soy tu primera app Web Flask"


if __name__ == '__main__':
    app.run(debug=True)
