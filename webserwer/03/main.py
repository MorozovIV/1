from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id =db.Column(db.Integer, primary_key=True) #уникальный ключ
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    datd = db.Column(db.DateTime(300), default=datetime.utcnow())

    def __repr__(self):
        return 'Article %r>' % self.id

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
