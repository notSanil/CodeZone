from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
#CHANGE THIS ON RELEASE


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run()