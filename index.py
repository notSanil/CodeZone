from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
#CHANGE THIS ON RELEASE


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/compete")
def compete():
    return render_template('compete.html')

@app.route("/leaderboard")
def leaderboard():
    return render_template('leaderboard.html')

@app.route("/practice")
def practice():
    return render_template('practice.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/trending")
def trending():
    return render_template('trending.html')


if __name__ == '__main__':
    app.run()