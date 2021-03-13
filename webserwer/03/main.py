from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "Hi, !" + name + "-" + str(id)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/down')
def down():
    return render_template("down.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000')
